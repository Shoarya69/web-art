from app.editing.blend_2 import blend
from app.editing.cartoon import cartoon
from app.editing.eadg import edge
from app.editing.gray_scale import gray
from app.editing.sharper import sharp
from app.editing.smoth import smoth
from flask import current_app


def editing(op,fp):
    output_path = current_app.config.get("Edited_output")
    out = output_path
    match op:
        case "gray":
            final = gray(fp,out)
        case "sharp":
            final = sharp(fp,out)
        case "smoth":
            final = smoth(fp,out)
        case "edge":
            final = edge(fp,out)
        case "cart":
            final = cartoon(fp,out)
        case _:
            final = None
    return final