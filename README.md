# cvs-2-arcgis
A python project to scrape API's for their content, and publish this to ArcGIS as a hosted feature layer. Currently very specific to the Thames Water API, and unable to publish with symbology, plans to improve it to be more adaptive/easier to implement with new APIs and include greater functionality.

Features:
+ Accesses API with credentials
+ Converts that fetched data into a format possible to publish on ArcGIS
+ Outputs this as a CVS file
+ Includes a separate script to publish that CVS file as a hosted feature layer, with a hosted CVS linked to it
+ Main script updates feature layer with new CVS details

Planned changes:
- Include a user interface script to configure a lightweight version of the mainscript, determining whether or not an initial publish needs to occur or not.
- Allow saving and recognition of APIs, linking each to a specific, clearly configurable script
- Streamline data handling
- Allow modifying symbology of layer (May well require using Excel instead of CVS)
- Allow modifying of metadata of core hosted feature layer
- More helpful readme to aid use and common pitfalls in generating a CVS suitable for ArcGIS upload.
