from .. import Yvann_tests
import re

class ConvertNodeBase(Yvann_tests):
    CATEGORY = "🧪 Yvann Tests/🔄 Convert"
    
class BboxStringToBboxesTuples(ConvertNodeBase) :
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "bbox_string": ("STRING", {"forceInput": True}),
            }
        }
    RETURN_TYPES = ("BBOX",)
    RETURN_NAMES = ("bboxes",)

    FUNCTION = "bbox_string_to_bboxes_tuples"
    
    def bbox_string_to_bboxes_tuples(self, bbox_string):
        bbox_str = str(bbox_string).strip()

        if (bbox_str.startswith("'") and bbox_str.endswith("'")) or \
           (bbox_str.startswith('"') and bbox_str.endswith('"')):
            bbox_str = bbox_str[1:-1]

        segments = re.findall(r'\[([^\]]+)\]', bbox_str)

        liste_tuples = []
        for segment in segments:
            try:
                nombres = tuple(int(num.strip()) for num in segment.split(','))

                if len(nombres) != 4:
                    print(f"Wrong Numbers given: {segment}")
                    continue

                liste_tuples.append(nombres)
            except ValueError as e:
                print(f"Error converting '{segment}': {e}")
                continue

        return (liste_tuples,)