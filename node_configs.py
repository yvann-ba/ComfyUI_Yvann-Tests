#NOTE: this abstraction allows for both the documentation to be centrally managed and inherited
from abc import ABCMeta
class NodeConfigMeta(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        if name in NODE_CONFIGS:
            for key, value in NODE_CONFIGS[name].items():
                setattr(new_class, key, value)
        return new_class

class CombinedMeta(NodeConfigMeta, ABCMeta):
    pass

def add_node_config(node_name, config):
    NODE_CONFIGS[node_name] = config

NODE_CONFIGS = {}

add_node_config("IPAdapter_Audio_Reactive", {
    "BASE_DESCRIPTION": """
Receives audio-reactive weights to control blending and switching between images based on audio peaks.\n
Returns images and associated weights to use with two IPAdapter batches, inspired by "IPAdapter Weights" from [IPAdapter_Plus](https://github.com/cubiq/ComfyUI_IPAdapter_plus).

**Inputs:**

- **images**: Batch of images for transitions; each switches on an audio peak
- **audio_weights**: List of audio-reactive weights from the "Audio Reactive" node

**Parameters:**

- **timing**: Blending timing function; different modes smooth weights differently
- **transition_frames**: Frames over which to blend between images
- **threshold**: Minimum height for a peak to be considered

**Outputs:**

- **image_1**: Starting image for a transition; connect to first IPAdapter batch image input
- **weights**: Blending weights for image transitions; connect to first IPAdapter batch weight input
- **image_2**: Ending image for a transition; connect to second IPAdapter batch image input
- **weights_invert**: Inverse blending weights; connect to second IPAdapter batch weight input
- **graph_audio_index**: Visualization of audio weights, detected peaks, and image transitions
"""
})