# Thanks to RyanOnTheInside, KJNodes, MTB, Fill, Akatz, Matheo, their works helped me a lot
from pathlib import Path
from aiohttp import web
from .node_configs import CombinedMeta
from collections import OrderedDict
from server import PromptServer

class Yvann_tests(metaclass=CombinedMeta):
    @classmethod
    def get_description(cls):
        footer = "\n\n"
        footer = "#### 🐙 Docs, Workflows and Code: [Yvann_tests-Nodes GitHub](https://github.com/yvann-ba/ComfyUI_Yvann-Tests)"
        footer += " 👁️ Tutorials: [Yvann Youtube](https://www.youtube.com/@yvann.mp4)\n"

        desc = ""

        if hasattr(cls, 'DESCRIPTION'):
            desc += f"{cls.DESCRIPTION}\n\n{footer}"
            return desc

        if hasattr(cls, 'TOP_DESCRIPTION'):
            desc += f"{cls.TOP_DESCRIPTION}\n\n"

        if hasattr(cls, "BASE_DESCRIPTION"):
            desc += cls.BASE_DESCRIPTION + "\n\n"

        additional_info = OrderedDict()
        for c in cls.mro()[::-1]:
            if hasattr(c, 'ADDITIONAL_INFO'):
                info = c.ADDITIONAL_INFO.strip()
                additional_info[c.__name__] = info

        if additional_info:
            desc += "\n\n".join(additional_info.values()) + "\n\n"

        if hasattr(cls, 'BOTTOM_DESCRIPTION'):
            desc += f"{cls.BOTTOM_DESCRIPTION}\n\n"

        desc += footer
        return desc

from .nodes.BboxStringToBboxesTuples import BboxStringToBboxesTuples



NODE_CLASS_MAPPINGS = {
    "Bbox String To Bboxes Tuples": BboxStringToBboxesTuples,
}

WEB_DIRECTORY = "./web/js"

NODE_DISPLAY_NAME_MAPPINGS = {
   "Bbox String To Bboxes Tuples": "Bbox String To Bboxes Tuples"
}

Yvann_tests_Print = """
🧪 Yvann Tests and experimentals Nodes"""

print("\033[38;5;195m" + Yvann_tests_Print +
      "\033[38;5;222m" + " : Loaded\n" + "\033[0m")


if hasattr(PromptServer, "instance"):
    # NOTE: we add an extra static path to avoid comfy mechanism
    # that loads every script in web.
    PromptServer.instance.app.add_routes(
        [web.static("/yvann_tests_web_async",
                    (Path(__file__).parent.absolute() / "yvann_tests_web_async").as_posix())]
    )

for node_name, node_class in NODE_CLASS_MAPPINGS.items():
    if hasattr(node_class, 'get_description'):
        desc = node_class.get_description()
        node_class.DESCRIPTION = desc

__all__ = ["NODE_CLASS_MAPPINGS",
           "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
