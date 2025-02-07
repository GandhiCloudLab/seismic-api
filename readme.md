# Seismic API

In this documentation, let’s explore how to access the seismic API.

## 1 Get Access Token 

Here we get the API Token through UI. (Need to find other way to get it permanently).

1. Access this URL in your browser.

https://developer.seismic.com/seismicsoftware/docs/authentication-1

2. Enter the value `IBM` in the below text box.
3. Click `Select Tenant` button
<img src="images/img-01.png">

It shows the below page.

4. Select the appropriate checkboxes for the required  permissions for token.
5. Click on `Get Token`

<img src="images/img-02.png">
<img src="images/img-03.png">

5. It should open a seismic login page. After you complete the login, it should show the below page.

6. Click on `Copy Token`. This is your token.

<img src="images/img-04.png">

## 2. Access the APIs.

Here is the list of APIs available.

https://developer.seismic.com/seismicsoftware/reference/reporting-contentsget


### 2.1 Sample API - Access Content

1. Here is the python file [01-seismic.py](./files/01-seismic.py) to access the APIs

```
import requests

token = "xxxx"
url = "https://api.seismic.com/reporting/v2/contents?limit=5"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)

print(response.text)

```

2. Replace the `token = "xxxx"` with the token that you retrieved in the previous section.

3. Run the python using `python seismic.py` command.

4. You may get output like this [01-output.json](./files/01-output.json)

```
[
    {
        "id": "89f5b66c-28b9-4c37-8bed-a10c4600580b",
        "instanceName": "watsonx Client Briefing",
        "libraryContentId": "763f41b4-8dd2-47d7-a8d4-cf8c90177cb5",
        "normalizedName": "watsonx Client Briefing",
        "originRepository": "Library",
        "repository": "WorkSpace",
        "workspaceContentId": "89f5b66c-28b9-4c37-8bed-a10c4600580b",
        "modifiedAt": "2025-01-27T09:12:08.547Z",
        "createdAt": "2024-10-17T12:59:55.127Z",
        "originApplication": null,
        "format": "pptx",
        "isDeleted": false
    },
    {
        "id": "9764e279-0294-4e00-b2d7-9af3b9ca9c18",
        "instanceName": "Cost of a Data Breach Report 2024 - Executive Summary (LiveDoc Version)",
        "libraryContentId": "f5abd0a9-8637-4d77-a604-4368c786baae",
        "normalizedName": "Cost of a Data Breach Report 2024 - Executive Summary (LiveDoc Version)",
        "originRepository": "Library",
        "repository": "WorkSpace",
        "workspaceContentId": "9764e279-0294-4e00-b2d7-9af3b9ca9c18",
        "modifiedAt": "2025-02-03T07:38:45.033Z",
        "createdAt": "2024-08-06T03:18:38.097Z",
        "originApplication": null,
        "format": "pdf",
        "isDeleted": false
    },
    {
        "id": "6b865a1e-f895-40d7-a943-2b6d4245c565",
        "instanceName": "zOS Platform Support - Solution Implementation Guide",
        "libraryContentId": "6b865a1e-f895-40d7-a943-2b6d4245c565",
        "normalizedName": "zOS Platform Support - Solution Implementation Guide",
        "originRepository": "Library",
        "repository": "Library",
        "workspaceContentId": null,
        "modifiedAt": "2024-07-11T10:47:57.520Z",
        "createdAt": "2020-09-07T11:40:40.403Z",
        "originApplication": null,
        "format": "url",
        "isDeleted": true
    },
    {
        "id": "a7cfa68e-ca50-437c-9766-6506855eb6c0",
        "instanceName": "grammys",
        "libraryContentId": null,
        "normalizedName": "grammys",
        "originRepository": "WorkSpace",
        "repository": "WorkSpace",
        "workspaceContentId": "a7cfa68e-ca50-437c-9766-6506855eb6c0",
        "modifiedAt": "2023-08-15T21:12:07.029Z",
        "createdAt": "2023-01-27T02:04:47.333Z",
        "originApplication": null,
        "format": "jpeg",
        "isDeleted": false
    },
    {
        "id": "7ec69a01-4a0a-44d0-9b66-34e4bd1000da",
        "instanceName": "Client Invitation Mail for TechU - Storage_MA_2020-Sep-11 - Miele",
        "libraryContentId": null,
        "normalizedName": "Client Invitation Mail for TechU - Storage_MA_2020-Sep-11 - Miele",
        "originRepository": "WorkSpace",
        "repository": "WorkSpace",
        "workspaceContentId": "7ec69a01-4a0a-44d0-9b66-34e4bd1000da",
        "modifiedAt": "2023-08-15T21:12:07.029Z",
        "createdAt": "2020-09-15T10:54:58.363Z",
        "originApplication": null,
        "format": "docx",
        "isDeleted": true
    }
]
```
### 2.2 Sample API - Search by file name and properties

1. Here is the python file [02-seismic-search.py](./files/02-seismic-search.py) to access the APIs

```
import requests

token = "xxxxx"

url = "https://api.seismic.com/search/v1/content/query?"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

search_term = "Envizi-Integration-Hub-Webinar",

# Request payload
payload = {
    "term": f"{search_term}",
    "options":{ 
            "searchFields":["name","properties"],
            "returnFields":["id", "name", "type", "downloadUrl", "applicationUrls"]
            },
    "pageSize": 10  # Number of results to return
}

response = requests.post(url, headers=headers, json=payload)

print(response.text)

```

2. Replace the `token = "xxxx"` with the token that you retrieved in the previous section.

3. Run the python using `python seismic.py` command.

4. You may get output like this [02-output.json](./files/02-output.json)

```
{
    "queryTimeInMs": 187,
    "serviceTimeInMs": 822,
    "totalCount": 10,
    "documents": [
        {
            "id": "8b08dda0-4750-4bbb-8a43-d86a8d3adf62",
            "name": "Envizi-Integration-Hub-Webinar",
            "type": "file",
            "downloadUrl": "https://cis-prod-bss.seismic.com/api/download/v1/blob?t=ibm&c=ibm&id=683c2964-e239-4668-a240-e1fb41677179&et=20250204130725&fn=683c2964-e239-4668-a240-e1fb41677179.MP4&sig=BjCfI1V4vw7GyRT%2Fn%2F%2FpetST19O4bhoGriTk415ldmA%3D",
            "applicationUrls": [
                {
                    "name": "DocCenter Universal Link",
                    "url": "https://ibm.seismic.com/Link/Content/DC8FX34Dg3Ppm8cD6FhC9PgXbqVP"
                },
                {
                    "name": "Content Manager Link",
                    "url": "https://ibm.seismic.com/app#/contentmanager/detail/1/8b08dda0-4750-4bbb-8a43-d86a8d3adf62/info/LIST/title?versionId=7bcc34da-0fad-405d-a078-b79228a3279c"
                }
            ]
        },
        {
            "id": "29f1b140-6651-4654-86d6-d634d2ac9fcc",
            "name": "Accelerate automation of ESG Data into Envizi using Integration Hub!-20240925_132915-Meeting Recording",
            "type": "file",
            "downloadUrl": "https://cis-prod-bss.seismic.com/api/download/v1/blob?t=ibm&c=ibm&id=659752df-fa6b-4c13-b568-80143417e90a&et=20250204130725&fn=659752df-fa6b-4c13-b568-80143417e90a.MP4&sig=WwUSrXu5ZbR%2FhHWqPYv5LtB1SmI9hKSo8HaxBuTyKvA%3D",
            "applicationUrls": [
                {
                    "name": "DocCenter Universal Link",
                    "url": "https://ibm.seismic.com/Link/Content/DCPDdqDRR4VfRGWCbbgdgWHTGqf3"
                },
                {
                    "name": "Content Manager Link",
                    "url": "https://ibm.seismic.com/app#/contentmanager/detail/1/29f1b140-6651-4654-86d6-d634d2ac9fcc/info/LIST/title?versionId=17952b9a-7f18-4a9d-8096-411fbc481ce2"
                }
            ]
        },
        {
            "id": "a1fe0c75-5eb3-4f13-ad5c-cd9c14468a22",
            "name": "Webinar - Accelerate your digital initiatives with real-time information via IBM Z Digital Integration Hub (zDIH)",
            "type": "url",
            "downloadUrl": "https://cis-prod-bss.seismic.com/api/download/v1/blob?t=ibm&c=ibm&id=c2fa640a-2977-4bf1-9a45-85c0cda45456&et=20250204130725&fn=c2fa640a-2977-4bf1-9a45-85c0cda45456.URL&sig=GXc2gVubekUMfLEI0EYvTDW5Fu%2B72p06A%2BRWglDM%2FIs%3D",
            "applicationUrls": [
                {
                    "name": "Content Manager Link",
                    "url": "https://ibm.seismic.com/app#/contentmanager/detail/1/a1fe0c75-5eb3-4f13-ad5c-cd9c14468a22/info/LIST/title?versionId=f44434f5-bc48-4836-8125-5f997a6cca00"
                }
            ]
        },
        {
            "id": "12269f25-8f1e-4f60-8a89-e6d657281fff",
            "name": "IBM Z Digital Integration Hub webinar invitation",
            "type": "file",
            "downloadUrl": "https://cis-prod-bss.seismic.com/api/download/v1/blob?t=ibm&c=ibm&id=23e734ee-2029-4807-87f3-26ac71d03720&et=20250204130725&fn=23e734ee-2029-4807-87f3-26ac71d03720.PDF&sig=PckcsnaPvBou%2B6HuMLvgInS%2BCTZwEBlxXt%2BFQrrV5Zg%3D",
            "applicationUrls": [
                {
                    "name": "Content Manager Link",
                    "url": "https://ibm.seismic.com/app#/contentmanager/detail/1/12269f25-8f1e-4f60-8a89-e6d657281fff/info/LIST/title?versionId=dcc19d15-5b91-4e49-84a2-8983eb0a08ce"
                }
            ]
        },
        {
            "id": "9f5585be-96e2-4175-bcb7-bc10b352093c",
            "name": "Envizi-Integration-Hub-2Minutes-Intro",
            "type": "file",
            "downloadUrl": "https://cis-prod-bss.seismic.com/api/download/v1/blob?t=ibm&c=ibm&id=2fc78046-4e90-41bb-a9af-8f5612f198ec&et=20250204130725&fn=2fc78046-4e90-41bb-a9af-8f5612f198ec.MP4&sig=kIJ2HHs1aMmxThqgCGepBTC5IJHcvT5U5yYK7fSN2Gw%3D",
            "applicationUrls": [
                {
                    "name": "DocCenter Universal Link",
                    "url": "https://ibm.seismic.com/Link/Content/DCcgD9TMqD6fg8F2Hcc3PTJ83QM3"
                },
                {
                    "name": "Content Manager Link",
                    "url": "https://ibm.seismic.com/app#/contentmanager/detail/1/9f5585be-96e2-4175-bcb7-bc10b352093c/info/LIST/title?versionId=efae5ecd-722d-4de0-8695-9372e18465d2"
                }
            ]
        },
        {
            "id": "1c7e06a5-f672-460a-9980-e5bb09f52094",
            "name": "Sustainability Software assets_One Pager-Envizi-IntegrationHub",
            "type": "file",
            "downloadUrl": "https://cis-prod-bss.seismic.com/api/download/v1/blob?t=ibm&c=ibm&id=b7c66db4-2408-4a17-8f91-a22e8f141540&et=20250204130725&fn=b7c66db4-2408-4a17-8f91-a22e8f141540.PPTX&sig=qj%2BGdU1etTvwAd3uUmxgblSIKc0tN2mTzORXOVo38Y8%3D",
            "applicationUrls": [
                {
                    "name": "DocCenter Universal Link",
                    "url": "https://ibm.seismic.com/Link/Content/DC88FMjMF6pdHGWJVBjbm37mQB63"
                },
                {
                    "name": "Content Manager Link",
                    "url": "https://ibm.seismic.com/app#/contentmanager/detail/1/1c7e06a5-f672-460a-9980-e5bb09f52094/info/LIST/title?versionId=411fdd74-ffc6-4d39-b928-f9bb39b5c164"
                }
            ]
        },
        {
            "id": "426f8e4d-d41a-4980-8ea9-4dcefdebdd50",
            "name": "IntegrationHub-Webinar",
            "type": "file",
            "downloadUrl": "https://cis-prod-bss.seismic.com/api/download/v1/blob?t=ibm&c=ibm&id=3a2ca30a-f45f-4ef3-abfc-05b0d56b4159&et=20250204130725&fn=3a2ca30a-f45f-4ef3-abfc-05b0d56b4159.PDF&sig=GtQ3jubIhvYtZLp4mqFuug%2B7rJYVNp%2BVEUQ6k968D60%3D",
            "applicationUrls": [
                {
                    "name": "DocCenter Universal Link",
                    "url": "https://ibm.seismic.com/Link/Content/DCQbMJp33gg6BG7F9QQcM2hgpmRB"
                },
                {
                    "name": "Content Manager Link",
                    "url": "https://ibm.seismic.com/app#/contentmanager/detail/1/426f8e4d-d41a-4980-8ea9-4dcefdebdd50/info/LIST/title?versionId=27ced84f-ed63-4e81-85a4-cd7bba28882e"
                }
            ]
        },
        {
            "id": "e0d775ed-27d1-4b98-882e-9d3ccf079121",
            "name": "Envizi Integration Hub",
            "type": "folder",
            "applicationUrls": [
                {
                    "name": "Content Manager Link",
                    "url": "https://ibm.seismic.com/app#/contentmanager/main/1/e0d775ed-27d1-4b98-882e-9d3ccf079121/LIST/title"
                }
            ]
        },
        {
            "id": "59d4d830-d036-4fc7-9696-077a4a4d6972",
            "name": "BP Relationship Revalidation 2024 Quick Reference Guide",
            "type": "file",
            "downloadUrl": "https://cis-prod-bss.seismic.com/api/download/v1/blob?t=ibm&c=ibm&id=9e1ae7c1-204f-4684-8fde-41d507af5880&et=20250204130725&fn=9e1ae7c1-204f-4684-8fde-41d507af5880.PPTX&sig=2BqnDf2qRy53LjAiDUuvI98BExe55pkyhqqRqh45nrg%3D",
            "applicationUrls": [
                {
                    "name": "Content Manager Link",
                    "url": "https://ibm.seismic.com/app#/contentmanager/detail/1/59d4d830-d036-4fc7-9696-077a4a4d6972/info/LIST/title?versionId=5f83758d-cf36-4dbe-9ba1-d2aa412693fd"
                }
            ]
        },
        {
            "id": "c96334b6-23ad-4c6e-bab1-fe8c370429e6",
            "name": "Powering Innovation in Hybrid Cloud with AI | Tech Mahindra X IBM",
            "type": "url",
            "downloadUrl": "https://cis-prod-bss.seismic.com/api/download/v1/blob?t=ibm&c=ibm&id=7e67a3be-af64-4cb3-908c-573efc86449e&et=20250204130725&fn=7e67a3be-af64-4cb3-908c-573efc86449e.YouTube&sig=04ha30yNKlBdLkWelEyK2T0l0yGhqqtUrp4aXIK0qzg%3D",
            "applicationUrls": [
                {
                    "name": "Content Manager Link",
                    "url": "https://ibm.seismic.com/app#/contentmanager/detail/1/c96334b6-23ad-4c6e-bab1-fe8c370429e6/info/LIST/title?versionId=23985cde-bdda-4b5f-9d6c-5b7235496021"
                }
            ]
        }
    ],
    "continuationToken": null
}
```
