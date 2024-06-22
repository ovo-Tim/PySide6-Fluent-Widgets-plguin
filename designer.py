import os
from pathlib import Path

plugin_path = Path(__file__).parent.joinpath("plugins")
os.environ["PYSIDE_DESIGNER_PLUGINS"] = str(plugin_path)

print(plugin_path)

os.system(f"cd { plugin_path } && pyside6-designer")
