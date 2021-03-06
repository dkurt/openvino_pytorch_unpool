from mo.front.extractor import FrontExtractorOp
from mo.front.onnx.extractors.utils import onnx_attr
from ...ops.FFT import FFT

class FFTFrontExtractor(FrontExtractorOp):
    op = 'FFT'
    enabled = True

    @classmethod
    def extract(cls, node):
        data = {
            'inverse': onnx_attr(node, 'inverse', 'i'),
        }

        FFT.update_node_stat(node, data)
        return cls.enabled
