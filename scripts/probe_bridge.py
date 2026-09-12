"""Reproduce upstream behavior before adding workbench adaptations."""
from pathlib import Path
import jpype
import orhelper

root = Path(__file__).resolve().parents[1]
with orhelper.OpenRocketInstance(
    jar=str(root / '.tools/OpenRocket-24.12.jar'),
    jvm='/Library/Java/JavaVirtualMachines/jdk-21.jdk/Contents/Home/lib/server/libjvm.dylib',
    loglevel='ERROR',
) as instance:
    helper = orhelper.Helper(instance)
    doc = helper.load_doc(str(root / 'examples/upstream-simple.ork'))
    sim = doc.getSimulation(0)
    sim.getOptions().setRandomSeed(42)
    helper.run_simulation(sim)
    print('seed after helper:', sim.getOptions().getRandomSeed())
    print('apogee:', sim.getSimulatedData().getMaxAltitude())
    print('warnings:', list(sim.getSimulatedData().getWarningSet()))
    print('events:', helper.get_events(sim))
    try:
        helper.run_simulation(sim, [orhelper.AbstractSimulationListener()])
        print('listener: passed')
    except Exception as exc:
        print('listener failure:', type(exc).__name__, str(exc))
    print('component names:', [str(c.getName()) for c in orhelper.JIterator(doc.getRocket())])
    print('Java:', jpype.java.lang.System.getProperty('java.runtime.version'))
