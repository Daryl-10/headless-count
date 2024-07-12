# headless-count

<h1>Extension to ["austere-snap" project](https://github.com/Daryl-10/austere-snap): Counting ships indicated by colored dots using Computer Vision</h1>

<h3>In this project, we use an automated script that:</h3>
<p>1) counts the number of vessels identified as magenta dots in the .png file provided</p>
--> <i>Able to reuse assets from "austere-snap" project</i>
<p>2) runs the aforementioned core feature in a Docker container</p>
--> <b>This will require some ancillary features to be omitted when building the Docker Image</b>


<h3>An extension feature is suggested: Log the number of vessels in a publicy exposed Google Sheets</h3>
<b>Credit to [Jie Jenn](https://learndataanalysis.org/writing-data-to-google-sheets-google-sheets-api-in-python-part-3/) for the following resources:</b>
<p>1) code snippet used in insert_to_sheet.py (shown in this repo)</p>
<p>2) code snippet used in Google.py (referenced, but not shown in this repo)</p>

---

<h2>On first run:</h2>
<h4>1) pip install virtual environment</h4>

`pip install virtualenv`

<h4>2) Set up virtual environment in project</h4>

`python<version> -m venv <virtual-environment-name>`

<h4>3) Activate virtual environment</h4>
<h4>4) Navigate to main directory and install from requirements.txt</h4>

`pip install -r requirements.txt`

---

<h3>Note that you should supply your own credentials & values for the following:</h3>
<h4>1) client_secrets.json</h4>
    <p>-> This is a preparation step to link the above 'service' to a Cloud Service provider. Sample format shown below is for Google Cloud project</p>

```json
    {"installed":
        {"client_id":"",
        "project_id":"",
        "auth_uri":"https://accounts.google.com/o/oauth2/auth",
        "token_uri":"https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
        "client_secret":"",
        "redirect_uris":["http://localhost"]
        }
    }
```

<h4>2) mycreds.txt</h4>
    <p>-> When running the code for the first time, mycreds.txt is generated after linking to a Cloud Service provider</p>
    <p>-> Afterwards, mycreds.txt is generated & reused for subsequent invokations.</p>
<h4>3) value for public_folder_id variable in upload.py</h4>
    <p>-> This is used to upload to a specific Google Drive folder. Set up for this publicly accessible folder should be done prior to running screengrab.py (& by extension, upload.py)</p>
<h4>4) value for spreadsheet_id variable in insert_to_sheet.py</h4>
    <p>-> This is used to upload to append values to the indicated Google Sheets. This allows processed values to be logged on a regular basis.</p>


---



<h3>Integrate Google Cloud CLI with Docker</h3>
<h4>1) gcloud init</h4>
<p>--> Log into gcloud using CLI: User Authentication will be done through browser</p>
<h4>2) Select appropriate gcloud project</h4>
<p>--> (Optional) It might be necessary to configure a default Compute Region and Zone that corresponds to that of the project's Artifact Registry</p>
<h4>3) Configure Docker with the credentials for the same Compute Region and Zone</h4>
<p>--> Sample code</p>

```
gcloud auth configure-docker us-central1-docker.pkg.dev
```

<p>--> Sample output</p>

```json
 {
  "credHelpers": {
    "us-central1-docker.pkg.dev": "gcloud"
  }
}
```

<h4>4) Build the Docker image</h4>
<p>Sample code below is for MacOS with M1 chip & above</p>

```
docker buildx build --platform linux/amd64 -t imgName .
```

<h4>5) Tag the Docker image</h4>

```
docker tag imgName us-central1-docker.pkg.dev/cloudProjName/artifactRegistry/imgName
```

<p><b>imgName</b> should correspond to the one above in Step 4</p>
<p><b>cloudProjName</b> is determined when creating the project in Google Cloud Console</p>
<p><b>artifactRegistry</b> is determined when creating the Artifact Registry in Google Cloud Console</p>

<p>The naming convention is used to push the Docker image to the intended directory in Artifact Registry</p>

<h4>6) Push the Docker image</h4>

```
docker push us-central1-docker.pkg.dev/cloudProjName/artifactRegistry/imgName
```

---
