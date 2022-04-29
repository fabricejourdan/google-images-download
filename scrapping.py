# importing google_images_download module
from google_images_download import google_images_download

# creating object
response = google_images_download.googleimagesdownload()

search_items = [
    {"query": "Lyon manifestation", "image_directory": "manifestation", "usage_rights": "labeled-for-reuse"},
    {"query": "Lyon manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-reuse-with-modifications"},
    {"query": "Lyon manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-nocommercial-reuse"},
    {"query": "Lyon manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    {"query": "Marseille manifestation", "image_directory": "manifestation", "usage_rights": "labeled-for-reuse"},
    {"query": "Marseille manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-reuse-with-modifications"},
    {"query": "Marseille manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-nocommercial-reuse"},
    {"query": "Marseille manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    {"query": "Paris manifestation", "image_directory": "manifestation", "usage_rights": "labeled-for-reuse"},
    {"query": "Paris manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-reuse-with-modifications"},
    {"query": "Paris manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-nocommercial-reuse"},
    {"query": "Paris manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    {"query": "Toulouse manifestation", "image_directory": "manifestation", "usage_rights": "labeled-for-reuse"},
    {"query": "Toulouse manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-reuse-with-modifications"},
    {"query": "Toulouse manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-nocommercial-reuse"},
    {"query": "Toulouse manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    {"query": "Nice manifestation", "image_directory": "manifestation", "usage_rights": "labeled-for-reuse"},
    {"query": "Nice manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-reuse-with-modifications"},
    {"query": "Nice manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-nocommercial-reuse"},
    {"query": "Nice manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    {"query": "Montpellier manifestation", "image_directory": "manifestation", "usage_rights": "labeled-for-reuse"},
    {"query": "Montpellier manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-reuse-with-modifications"},
    {"query": "Montpellier manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-nocommercial-reuse"},
    {"query": "Montpellier manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    {"query": "Nantes manifestation", "image_directory": "manifestation", "usage_rights": "labeled-for-reuse"},
    {"query": "Nantes manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-reuse-with-modifications"},
    {"query": "Nantes manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-nocommercial-reuse"},
    {"query": "Nantes manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    {"query": "Strasbourg manifestation", "image_directory": "manifestation", "usage_rights": "labeled-for-reuse"},
    {"query": "Strasbourg manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-reuse-with-modifications"},
    {"query": "Strasbourg manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-nocommercial-reuse"},
    {"query": "Strasbourg manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    {"query": "Bordeaux manifestation", "image_directory": "manifestation", "usage_rights": "labeled-for-reuse"},
    {"query": "Bordeaux manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-reuse-with-modifications"},
    {"query": "Bordeaux manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-nocommercial-reuse"},
    {"query": "Bordeaux manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    {"query": "Lille manifestation", "image_directory": "manifestation", "usage_rights": "labeled-for-reuse"},
    {"query": "Lille manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-reuse-with-modifications"},
    {"query": "Lille manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-nocommercial-reuse"},
    {"query": "Lille manifestation", "image_directory": "manifestation",
     "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
]

# Driver Code
for search_item in search_items:
    query = search_item["query"]
    print('query:', query)
    usage_rights = search_item["usage_rights"]
    print('usage_rights:', usage_rights)
    if 'image_directory' in search_item and search_item["image_directory"].strip() != '':
        image_directory = search_item["image_directory"]
    else:
        image_directory = query.replace(' ', '_') + '_' + usage_rights
    print('image_directory:', image_directory)
    # keywords is the search query
    # format is the image file format
    # limit is the number of images to be downloaded
    # print urs is to print the image file url
    # size is the image size which can
    # be specified manually ("large, medium, icon")
    arguments = {"keywords": query,
                 "format": "jpg",
                 "limit": 150,
                 "print_urls": True,
                 "chromedriver": "chromedriver.exe",
                 "image_directory": image_directory,
                 "usage_rights": usage_rights,
                 # "size": "medium",
                 }
    try:
        response.download(arguments)

    # Handling File NotFound Error
    except FileNotFoundError:
        print('FileNotFoundError')
        pass

print("That's all folks!")
