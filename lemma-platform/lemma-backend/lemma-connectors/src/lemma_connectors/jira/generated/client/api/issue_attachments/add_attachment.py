from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.attachment import Attachment
from ...types import File, FileTypes
from ...types import UNSET, Unset
from io import BytesIO
from typing import cast



def _get_kwargs(
    issue_id_or_key: str,
    *,
    body:    File  |     File  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/issue/{issue_id_or_key}/attachments".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),),
    }

    if isinstance(body, File):
        

        headers["Content-Type"] = "multipart/form-data"
    if isinstance(body, File):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_tuple()



        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[Attachment] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = Attachment.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[Attachment]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    body:    File  |     File  | Unset = UNSET,

) -> Response[Any | list[Attachment]]:
    r""" Add attachment

     Adds one or more attachments to an issue. Attachments are posted as multipart/form-data ([RFC
    1867](https://www.ietf.org/rfc/rfc1867.txt)).

    Note that:

     *  The request must have a `X-Atlassian-Token: no-check` header, if not it is blocked. See [Special
    headers](#special-request-headers) for more information.
     *  The name of the multipart/form-data parameter that contains the attachments must be `file`.

    The following examples upload a file called *myfile.txt* to the issue *TEST-123*:

    #### curl ####

        curl --location --request POST 'https://your-
    domain.atlassian.net/rest/api/3/issue/TEST-123/attachments'
         -u 'email@example.com:<api_token>'
         -H 'X-Atlassian-Token: no-check'
         --form 'file=@\"myfile.txt\"'

    #### Node.js ####

        // This code sample uses the 'node-fetch' and 'form-data' libraries:
         // https://www.npmjs.com/package/node-fetch
         // https://www.npmjs.com/package/form-data
         const fetch = require('node-fetch');
         const FormData = require('form-data');
         const fs = require('fs');

         const filePath = 'myfile.txt';
         const form = new FormData();
         const stats = fs.statSync(filePath);
         const fileSizeInBytes = stats.size;
         const fileStream = fs.createReadStream(filePath);

         form.append('file', fileStream, {knownLength: fileSizeInBytes});

         fetch('https://your-domain.atlassian.net/rest/api/3/issue/TEST-123/attachments', {
             method: 'POST',
             body: form,
             headers: {
                 'Authorization': `Basic ${Buffer.from(
                     'email@example.com:'
                 ).toString('base64')}`,
                 'Accept': 'application/json',
                 'X-Atlassian-Token': 'no-check'
             }
         })
             .then(response => {
                 console.log(
                     `Response: ${response.status} ${response.statusText}`
                 );
                 return response.text();
             })
             .then(text => console.log(text))
             .catch(err => console.error(err));

    #### Java ####

        // This code sample uses the  'Unirest' library:
         // http://unirest.io/java.html
         HttpResponse response = Unirest.post(\"https://your-
    domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments\")
                 .basicAuth(\"email@example.com\", \"\")
                 .header(\"Accept\", \"application/json\")
                 .header(\"X-Atlassian-Token\", \"no-check\")
                 .field(\"file\", new File(\"myfile.txt\"))
                 .asJson();

                 System.out.println(response.getBody());

    #### Python ####

        # This code sample uses the 'requests' library:
         # http://docs.python-requests.org
         import requests
         from requests.auth import HTTPBasicAuth
         import json

         url = \"https://your-domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments\"

         auth = HTTPBasicAuth(\"email@example.com\", \"\")

         headers = {
            \"Accept\": \"application/json\",
            \"X-Atlassian-Token\": \"no-check\"
         }

         response = requests.request(
            \"POST\",
            url,
            headers = headers,
            auth = auth,
            files = {
                 \"file\": (\"myfile.txt\", open(\"myfile.txt\",\"rb\"), \"application-type\")
            }
         )

         print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(\",\", \":
    \")))

    #### PHP ####

        // This code sample uses the 'Unirest' library:
         // http://unirest.io/php.html
         Unirest\Request::auth('email@example.com', '');

         $headers = array(
           'Accept' => 'application/json',
           'X-Atlassian-Token' => 'no-check'
         );

         $parameters = array(
           'file' => File::add('myfile.txt')
         );

         $response = Unirest\Request::post(
           'https://your-domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments',
           $headers,
           $parameters
         );

         var_dump($response)

    #### Forge ####

        // This sample uses Atlassian Forge and the `form-data` library.
         // https://developer.atlassian.com/platform/forge/
         // https://www.npmjs.com/package/form-data
         import api from \"@forge/api\";
         import FormData from \"form-data\";

         const form = new FormData();
         form.append('file', fileStream, {knownLength: fileSizeInBytes});

         const response = await api.asApp().requestJira('/rest/api/2/issue/{issueIdOrKey}/attachments',
    {
             method: 'POST',
             body: form,
             headers: {
                 'Accept': 'application/json',
                 'X-Atlassian-Token': 'no-check'
             }
         });

         console.log(`Response: ${response.status} ${response.statusText}`);
         console.log(await response.json());

    Tip: Use a client library. Many client libraries have classes for handling multipart POST
    operations. For example, in Java, the Apache HTTP Components library provides a
    [MultiPartEntity](http://hc.apache.org/httpcomponents-client-
    ga/httpmime/apidocs/org/apache/http/entity/mime/MultipartEntity.html) class for multipart POST
    operations.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse Projects* and *Create attachments* [ project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        body (File | Unset):
        body (File | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[Attachment]]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    body:    File  |     File  | Unset = UNSET,

) -> Any | list[Attachment] | None:
    r""" Add attachment

     Adds one or more attachments to an issue. Attachments are posted as multipart/form-data ([RFC
    1867](https://www.ietf.org/rfc/rfc1867.txt)).

    Note that:

     *  The request must have a `X-Atlassian-Token: no-check` header, if not it is blocked. See [Special
    headers](#special-request-headers) for more information.
     *  The name of the multipart/form-data parameter that contains the attachments must be `file`.

    The following examples upload a file called *myfile.txt* to the issue *TEST-123*:

    #### curl ####

        curl --location --request POST 'https://your-
    domain.atlassian.net/rest/api/3/issue/TEST-123/attachments'
         -u 'email@example.com:<api_token>'
         -H 'X-Atlassian-Token: no-check'
         --form 'file=@\"myfile.txt\"'

    #### Node.js ####

        // This code sample uses the 'node-fetch' and 'form-data' libraries:
         // https://www.npmjs.com/package/node-fetch
         // https://www.npmjs.com/package/form-data
         const fetch = require('node-fetch');
         const FormData = require('form-data');
         const fs = require('fs');

         const filePath = 'myfile.txt';
         const form = new FormData();
         const stats = fs.statSync(filePath);
         const fileSizeInBytes = stats.size;
         const fileStream = fs.createReadStream(filePath);

         form.append('file', fileStream, {knownLength: fileSizeInBytes});

         fetch('https://your-domain.atlassian.net/rest/api/3/issue/TEST-123/attachments', {
             method: 'POST',
             body: form,
             headers: {
                 'Authorization': `Basic ${Buffer.from(
                     'email@example.com:'
                 ).toString('base64')}`,
                 'Accept': 'application/json',
                 'X-Atlassian-Token': 'no-check'
             }
         })
             .then(response => {
                 console.log(
                     `Response: ${response.status} ${response.statusText}`
                 );
                 return response.text();
             })
             .then(text => console.log(text))
             .catch(err => console.error(err));

    #### Java ####

        // This code sample uses the  'Unirest' library:
         // http://unirest.io/java.html
         HttpResponse response = Unirest.post(\"https://your-
    domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments\")
                 .basicAuth(\"email@example.com\", \"\")
                 .header(\"Accept\", \"application/json\")
                 .header(\"X-Atlassian-Token\", \"no-check\")
                 .field(\"file\", new File(\"myfile.txt\"))
                 .asJson();

                 System.out.println(response.getBody());

    #### Python ####

        # This code sample uses the 'requests' library:
         # http://docs.python-requests.org
         import requests
         from requests.auth import HTTPBasicAuth
         import json

         url = \"https://your-domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments\"

         auth = HTTPBasicAuth(\"email@example.com\", \"\")

         headers = {
            \"Accept\": \"application/json\",
            \"X-Atlassian-Token\": \"no-check\"
         }

         response = requests.request(
            \"POST\",
            url,
            headers = headers,
            auth = auth,
            files = {
                 \"file\": (\"myfile.txt\", open(\"myfile.txt\",\"rb\"), \"application-type\")
            }
         )

         print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(\",\", \":
    \")))

    #### PHP ####

        // This code sample uses the 'Unirest' library:
         // http://unirest.io/php.html
         Unirest\Request::auth('email@example.com', '');

         $headers = array(
           'Accept' => 'application/json',
           'X-Atlassian-Token' => 'no-check'
         );

         $parameters = array(
           'file' => File::add('myfile.txt')
         );

         $response = Unirest\Request::post(
           'https://your-domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments',
           $headers,
           $parameters
         );

         var_dump($response)

    #### Forge ####

        // This sample uses Atlassian Forge and the `form-data` library.
         // https://developer.atlassian.com/platform/forge/
         // https://www.npmjs.com/package/form-data
         import api from \"@forge/api\";
         import FormData from \"form-data\";

         const form = new FormData();
         form.append('file', fileStream, {knownLength: fileSizeInBytes});

         const response = await api.asApp().requestJira('/rest/api/2/issue/{issueIdOrKey}/attachments',
    {
             method: 'POST',
             body: form,
             headers: {
                 'Accept': 'application/json',
                 'X-Atlassian-Token': 'no-check'
             }
         });

         console.log(`Response: ${response.status} ${response.statusText}`);
         console.log(await response.json());

    Tip: Use a client library. Many client libraries have classes for handling multipart POST
    operations. For example, in Java, the Apache HTTP Components library provides a
    [MultiPartEntity](http://hc.apache.org/httpcomponents-client-
    ga/httpmime/apidocs/org/apache/http/entity/mime/MultipartEntity.html) class for multipart POST
    operations.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse Projects* and *Create attachments* [ project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        body (File | Unset):
        body (File | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[Attachment]
     """


    return sync_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    body:    File  |     File  | Unset = UNSET,

) -> Response[Any | list[Attachment]]:
    r""" Add attachment

     Adds one or more attachments to an issue. Attachments are posted as multipart/form-data ([RFC
    1867](https://www.ietf.org/rfc/rfc1867.txt)).

    Note that:

     *  The request must have a `X-Atlassian-Token: no-check` header, if not it is blocked. See [Special
    headers](#special-request-headers) for more information.
     *  The name of the multipart/form-data parameter that contains the attachments must be `file`.

    The following examples upload a file called *myfile.txt* to the issue *TEST-123*:

    #### curl ####

        curl --location --request POST 'https://your-
    domain.atlassian.net/rest/api/3/issue/TEST-123/attachments'
         -u 'email@example.com:<api_token>'
         -H 'X-Atlassian-Token: no-check'
         --form 'file=@\"myfile.txt\"'

    #### Node.js ####

        // This code sample uses the 'node-fetch' and 'form-data' libraries:
         // https://www.npmjs.com/package/node-fetch
         // https://www.npmjs.com/package/form-data
         const fetch = require('node-fetch');
         const FormData = require('form-data');
         const fs = require('fs');

         const filePath = 'myfile.txt';
         const form = new FormData();
         const stats = fs.statSync(filePath);
         const fileSizeInBytes = stats.size;
         const fileStream = fs.createReadStream(filePath);

         form.append('file', fileStream, {knownLength: fileSizeInBytes});

         fetch('https://your-domain.atlassian.net/rest/api/3/issue/TEST-123/attachments', {
             method: 'POST',
             body: form,
             headers: {
                 'Authorization': `Basic ${Buffer.from(
                     'email@example.com:'
                 ).toString('base64')}`,
                 'Accept': 'application/json',
                 'X-Atlassian-Token': 'no-check'
             }
         })
             .then(response => {
                 console.log(
                     `Response: ${response.status} ${response.statusText}`
                 );
                 return response.text();
             })
             .then(text => console.log(text))
             .catch(err => console.error(err));

    #### Java ####

        // This code sample uses the  'Unirest' library:
         // http://unirest.io/java.html
         HttpResponse response = Unirest.post(\"https://your-
    domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments\")
                 .basicAuth(\"email@example.com\", \"\")
                 .header(\"Accept\", \"application/json\")
                 .header(\"X-Atlassian-Token\", \"no-check\")
                 .field(\"file\", new File(\"myfile.txt\"))
                 .asJson();

                 System.out.println(response.getBody());

    #### Python ####

        # This code sample uses the 'requests' library:
         # http://docs.python-requests.org
         import requests
         from requests.auth import HTTPBasicAuth
         import json

         url = \"https://your-domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments\"

         auth = HTTPBasicAuth(\"email@example.com\", \"\")

         headers = {
            \"Accept\": \"application/json\",
            \"X-Atlassian-Token\": \"no-check\"
         }

         response = requests.request(
            \"POST\",
            url,
            headers = headers,
            auth = auth,
            files = {
                 \"file\": (\"myfile.txt\", open(\"myfile.txt\",\"rb\"), \"application-type\")
            }
         )

         print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(\",\", \":
    \")))

    #### PHP ####

        // This code sample uses the 'Unirest' library:
         // http://unirest.io/php.html
         Unirest\Request::auth('email@example.com', '');

         $headers = array(
           'Accept' => 'application/json',
           'X-Atlassian-Token' => 'no-check'
         );

         $parameters = array(
           'file' => File::add('myfile.txt')
         );

         $response = Unirest\Request::post(
           'https://your-domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments',
           $headers,
           $parameters
         );

         var_dump($response)

    #### Forge ####

        // This sample uses Atlassian Forge and the `form-data` library.
         // https://developer.atlassian.com/platform/forge/
         // https://www.npmjs.com/package/form-data
         import api from \"@forge/api\";
         import FormData from \"form-data\";

         const form = new FormData();
         form.append('file', fileStream, {knownLength: fileSizeInBytes});

         const response = await api.asApp().requestJira('/rest/api/2/issue/{issueIdOrKey}/attachments',
    {
             method: 'POST',
             body: form,
             headers: {
                 'Accept': 'application/json',
                 'X-Atlassian-Token': 'no-check'
             }
         });

         console.log(`Response: ${response.status} ${response.statusText}`);
         console.log(await response.json());

    Tip: Use a client library. Many client libraries have classes for handling multipart POST
    operations. For example, in Java, the Apache HTTP Components library provides a
    [MultiPartEntity](http://hc.apache.org/httpcomponents-client-
    ga/httpmime/apidocs/org/apache/http/entity/mime/MultipartEntity.html) class for multipart POST
    operations.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse Projects* and *Create attachments* [ project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        body (File | Unset):
        body (File | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[Attachment]]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    body:    File  |     File  | Unset = UNSET,

) -> Any | list[Attachment] | None:
    r""" Add attachment

     Adds one or more attachments to an issue. Attachments are posted as multipart/form-data ([RFC
    1867](https://www.ietf.org/rfc/rfc1867.txt)).

    Note that:

     *  The request must have a `X-Atlassian-Token: no-check` header, if not it is blocked. See [Special
    headers](#special-request-headers) for more information.
     *  The name of the multipart/form-data parameter that contains the attachments must be `file`.

    The following examples upload a file called *myfile.txt* to the issue *TEST-123*:

    #### curl ####

        curl --location --request POST 'https://your-
    domain.atlassian.net/rest/api/3/issue/TEST-123/attachments'
         -u 'email@example.com:<api_token>'
         -H 'X-Atlassian-Token: no-check'
         --form 'file=@\"myfile.txt\"'

    #### Node.js ####

        // This code sample uses the 'node-fetch' and 'form-data' libraries:
         // https://www.npmjs.com/package/node-fetch
         // https://www.npmjs.com/package/form-data
         const fetch = require('node-fetch');
         const FormData = require('form-data');
         const fs = require('fs');

         const filePath = 'myfile.txt';
         const form = new FormData();
         const stats = fs.statSync(filePath);
         const fileSizeInBytes = stats.size;
         const fileStream = fs.createReadStream(filePath);

         form.append('file', fileStream, {knownLength: fileSizeInBytes});

         fetch('https://your-domain.atlassian.net/rest/api/3/issue/TEST-123/attachments', {
             method: 'POST',
             body: form,
             headers: {
                 'Authorization': `Basic ${Buffer.from(
                     'email@example.com:'
                 ).toString('base64')}`,
                 'Accept': 'application/json',
                 'X-Atlassian-Token': 'no-check'
             }
         })
             .then(response => {
                 console.log(
                     `Response: ${response.status} ${response.statusText}`
                 );
                 return response.text();
             })
             .then(text => console.log(text))
             .catch(err => console.error(err));

    #### Java ####

        // This code sample uses the  'Unirest' library:
         // http://unirest.io/java.html
         HttpResponse response = Unirest.post(\"https://your-
    domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments\")
                 .basicAuth(\"email@example.com\", \"\")
                 .header(\"Accept\", \"application/json\")
                 .header(\"X-Atlassian-Token\", \"no-check\")
                 .field(\"file\", new File(\"myfile.txt\"))
                 .asJson();

                 System.out.println(response.getBody());

    #### Python ####

        # This code sample uses the 'requests' library:
         # http://docs.python-requests.org
         import requests
         from requests.auth import HTTPBasicAuth
         import json

         url = \"https://your-domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments\"

         auth = HTTPBasicAuth(\"email@example.com\", \"\")

         headers = {
            \"Accept\": \"application/json\",
            \"X-Atlassian-Token\": \"no-check\"
         }

         response = requests.request(
            \"POST\",
            url,
            headers = headers,
            auth = auth,
            files = {
                 \"file\": (\"myfile.txt\", open(\"myfile.txt\",\"rb\"), \"application-type\")
            }
         )

         print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(\",\", \":
    \")))

    #### PHP ####

        // This code sample uses the 'Unirest' library:
         // http://unirest.io/php.html
         Unirest\Request::auth('email@example.com', '');

         $headers = array(
           'Accept' => 'application/json',
           'X-Atlassian-Token' => 'no-check'
         );

         $parameters = array(
           'file' => File::add('myfile.txt')
         );

         $response = Unirest\Request::post(
           'https://your-domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments',
           $headers,
           $parameters
         );

         var_dump($response)

    #### Forge ####

        // This sample uses Atlassian Forge and the `form-data` library.
         // https://developer.atlassian.com/platform/forge/
         // https://www.npmjs.com/package/form-data
         import api from \"@forge/api\";
         import FormData from \"form-data\";

         const form = new FormData();
         form.append('file', fileStream, {knownLength: fileSizeInBytes});

         const response = await api.asApp().requestJira('/rest/api/2/issue/{issueIdOrKey}/attachments',
    {
             method: 'POST',
             body: form,
             headers: {
                 'Accept': 'application/json',
                 'X-Atlassian-Token': 'no-check'
             }
         });

         console.log(`Response: ${response.status} ${response.statusText}`);
         console.log(await response.json());

    Tip: Use a client library. Many client libraries have classes for handling multipart POST
    operations. For example, in Java, the Apache HTTP Components library provides a
    [MultiPartEntity](http://hc.apache.org/httpcomponents-client-
    ga/httpmime/apidocs/org/apache/http/entity/mime/MultipartEntity.html) class for multipart POST
    operations.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse Projects* and *Create attachments* [ project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        body (File | Unset):
        body (File | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[Attachment]
     """


    return (await asyncio_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,
body=body,

    )).parsed
