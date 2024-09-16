from typing import Annotated

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from .routers import items


app = FastAPI(
    title='FastAPI模板',
    summary='FastAPI项目模版',
    description='''\
* 使用漂亮的Elements Doc代替内置的Swagger UI
''',
    version='1.0.0',
    docs_url=None,  # disable default docs ui
    redoc_url=None, # disable default docs ui
)


app.include_router(items.router)
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get(
    '/docs',
    include_in_schema=False,
)
async def custom_swagger_ui_html() -> HTMLResponse:
    """
    ref: https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/
    :return: HTMLResponse
    """
    html = f'''\
<!doctype html>
<html lang="zh">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>{app.title}</title>

    <link rel="icon" type="	image/svg+xml" href="/static/elements/activity.svg"/>
    <link rel="stylesheet" href="static/elements/styles.min.css">
    <script src="static/elements/web-components.min.js"></script>
  </head>
  <body>

    <elements-api
      apiDescriptionUrl="{app.openapi_url}"
      router="hash"
      logo="/static/elements/activity.svg"
    />

  </body>
</html>
    '''
    return HTMLResponse(html)


@app.get(
    "/",
    summary='接口说明',
    response_description='应用信息',
    deprecated=True
)
async def root():
    """
    查看服务名称，服务版本
    """
    return {
        'app': app.title,
        'version': app.version
    }

