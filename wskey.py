import base64
import lzma

exec(lzma.decompress(base64.b64decode('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')))
