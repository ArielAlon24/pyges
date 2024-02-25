from enum import Enum


class FileType(Enum):
    # Document types
    HTML = "text/html"
    TXT = "text/plain"
    CSS = "text/css"
    JS = "application/javascript"
    JSON = "application/json"
    XML = "application/xml"
    PDF = "application/pdf"
    MD = "text/markdown"

    # Image types
    JPG = "image/jpeg"
    JPEG = "image/jpeg"
    PNG = "image/png"
    GIF = "image/gif"
    SVG = "image/svg+xml"
    WEBP = "image/webp"

    # Audio types
    MP3 = "audio/mpeg"
    WAV = "audio/wav"

    # Video types
    MP4 = "video/mp4"
    AVI = "video/x-msvideo"
    MOV = "video/quicktime"

    # Font types
    TTF = "font/ttf"
    OTF = "font/otf"
    WOFF = "font/woff"
    WOFF2 = "font/woff2"
    EOT = "application/vnd.ms-fontobject"

    # Archive types
    ZIP = "application/zip"
    RAR = "application/vnd.rar"
    _7Z = "application/x-7z-compressed"

    # Miscellaneous types
    CSV = "text/csv"
    RTF = "application/rtf"
    YAML = "application/x-yaml"
