// Independent evidence executable, not a Java replacement for the Python bridge.
// API: OpenRocket release-24.12, GPL-3.0 project, see docs/THIRD_PARTY.md.
import java.io.File;
import java.lang.reflect.Field;
import com.google.inject.Guice;
import info.openrocket.core.startup.Application;
import info.openrocket.core.plugin.PluginModule;
import info.openrocket.swing.startup.GuiModule;
import info.openrocket.core.database.AsynchronousDatabaseLoader;
import info.openrocket.core.file.GeneralRocketLoader;
import info.openrocket.core.simulation.FlightDataType;

class ReferenceCheck {
    public static void main(String[] args) throws Exception {
        var gui = new GuiModule();
        Application.setInjector(Guice.createInjector(gui, new PluginModule()));
        gui.startLoader();
        for (String name : new String[]{"presetLoader", "motorLoader"}) {
            Field f = GuiModule.class.getDeclaredField(name);
            f.setAccessible(true);
            ((AsynchronousDatabaseLoader)f.get(gui)).blockUntilLoaded();
        }
        var doc = new GeneralRocketLoader(new File(args[0])).load();
        var sim = doc.getSimulation(0);
        sim.getOptions().setRandomSeed(42);
        sim.simulate();
        var branch = sim.getSimulatedData().getBranch(0);
        double maximum = branch.get(FlightDataType.TYPE_ALTITUDE).stream().mapToDouble(Double::doubleValue).max().orElseThrow();
        System.out.println("REFERENCE_JSON={\"apogee_m\":"+maximum+
            ",\"samples\":"+branch.get(FlightDataType.TYPE_TIME).size()+
            ",\"warning_count\":"+sim.getSimulatedData().getWarningSet().size()+
            ",\"guide_departure_m_s\":"+sim.getSimulatedData().getLaunchRodVelocity()+
            ",\"deployment_speed_m_s\":"+sim.getSimulatedData().getDeploymentVelocity()+
            ",\"landing_total_speed_m_s\":"+sim.getSimulatedData().getGroundHitVelocity()+
            ",\"time_s\":"+branch.get(FlightDataType.TYPE_TIME)+
            ",\"altitude_m\":"+branch.get(FlightDataType.TYPE_ALTITUDE)+"}");
        System.exit(0);
    }
}
