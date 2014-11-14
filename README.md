data-from-papers
================

An index linking journal publications to the individual datasets from data-sharing repositories that they used.

This repository tracks publications that make use of data from data-sharing repositories, and in-particular the individual data-sets that the publications use.


For a publication identifier (DOI or pubmed ID) track:

 - citation information for the paper
 - paper abstract
 - list of data used in the publication: DOI for the dataset used, datset subject ids
 
 For each data repository / study (indexed by doi?):

 - abstract for the repository
 - list of all individual datasets available
 - provide a means to create links to the data(??)
 
 Create a webpage:
 
 - provides a query mechanism where can search by publication identifier
 - A publication page that displays the citation, abstract and list of data.
 - Provides a download that is a .json or .csv file that contains the list of data a long with their S3 tags if they exist
 - Provide a submission process, that minimizes the amount of information that the user needs to submit - user submits DOI or PUBMID for the paper, upload data in a CSV (doi:subid?, just a list of subids?, how do you indicate the study?, is the subject list compared to the study to make sure that the subject exists?, is the user asked to provide links to each of the data, or can it be determined from the study information? at what level is a DOI applied to the shared data? for example with preprocessed data?)
 
 Create a RESTful API:

 - allow the scriptable query the repository
 - allow upload of data to the repository via REST??
 
 