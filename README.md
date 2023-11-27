# cvs-2-arcgis
A python project to scrape API's for their content, and publish this to ArcGIS as a hosted feature layer. Currently very specific to the Thames Water API, and unable to publish with symbology, plans to improve it to be more adaptive/easier to implement with new APIs and include greater functionality.

**Features:**
+ Accesses API with credentials.
+ Converts that fetched data into a format possible to publish on ArcGIS.
+ Outputs this as a CVS file.
+ Includes a separate script to publish that CVS file as a hosted feature layer, with a hosted CVS linked to it.
+ Main script updates feature layer with new CVS details.

**Planned changes:**
- Include a user interface script to configure a lightweight version of the mainscript, determining whether or not an initial publish needs to occur or not and selecting appropriate data handling scripts.
- Allow saving and recognition of APIs, linking each to a specific, clearly configurable script.
- Streamline data handling.
- Allow modifying symbology of layer (May well require using Excel instead of CVS).
- Allow modifying of metadata of core hosted feature layer.
- More helpful readme to aid use and common pitfalls in generating a CVS suitable for ArcGIS upload.
- Package with ArcGIS to avoid dependency on Anaconda3.

**Dependencies**
Software
- Anaconda3: Necessary to install the 'arcgis' module.
- Python 3.11.5: 'convertbng' module is not yet updated to Python 3.12 .
Python modules:
- requests: in order to access APIs and request contents.
- pandas: handles API data as a dataframe and outputs to csv.
- arcgis: interacts with ArcGIS website
- convertbng: used in the Thames Water API to convert coordinates from British National Grid to WGS 1984, necessary for plotting on ArcGIS online.

UPLOADING PROJECT TOMORROW!

Many thanks to Thames Water for making the initial data online available through their API, all the module and software developers, the ArcGIS documentation, as well as the online python community.
