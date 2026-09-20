import json
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs/assets/integrated-fin-collar-v1"


def test_integrated_fin_collar_source_and_x1c_project_are_present_and_valid():
    for name in ("collar-fins.f3d", "collar-fins.step", "collar-fins.stl", "integrated-fin-collar-preview.png"):
        assert (ASSETS / name).is_file()

    with ZipFile(ASSETS / "integrated-fin-collar-X1C-PLA-review.3mf") as project:
        assert project.testzip() is None
        settings = json.loads(project.read("Metadata/project_settings.config"))
        assert settings["printer_model"] == "Bambu Lab X1 Carbon"
        assert settings["nozzle_diameter"] == ["0.4"]
        assert settings["layer_height"] == "0.2"
        assert settings["wall_loops"] == "4"
        assert settings["sparse_infill_density"] == "40%"
        assert settings["sparse_infill_pattern"] == "gyroid"
        assert settings["brim_width"] == "5"

        # This is an editable project, not retained sliced toolpath evidence.
        assert not any(name.endswith(".gcode") for name in project.namelist())
