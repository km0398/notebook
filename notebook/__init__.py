<table class="tfo-notebook-buttons" align="left">
  <td>
    <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/01-3.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
  </td>
  <td>
    <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/01-3.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
  </td>
</table>
#--------------------------------------------------------------------------------------------------------
from __future__ import annotations

from typing import Any

from ._version import __version__  # noqa: F401


def _jupyter_server_extension_paths() -> list[dict[str, str]]:
    return [{"module": "notebook"}]


def _jupyter_server_extension_points() -> list[dict[str, Any]]:
    from .app import JupyterNotebookApp

    return [{"module": "notebook", "app": JupyterNotebookApp}]


def _jupyter_labextension_paths() -> list[dict[str, str]]:
    return [{"src": "labextension", "dest": "@jupyter-notebook/lab-extension"}]
