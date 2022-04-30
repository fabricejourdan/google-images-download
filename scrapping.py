# importing google_images_download module
from google_images_download import google_images_download

# creating object
response = google_images_download.googleimagesdownload()

search_items = [
    {"query": "images de video surveillance en ville", "image_directory": "surveillance",
     "usage_rights": "labeled-for-reuse"},
    {"query": "images de video surveillance en ville", "image_directory": "surveillance",
     "usage_rights": "labeled-for-reuse-with-modifications"},
    {"query": "images de video surveillance en ville", "image_directory": "surveillance",
     "usage_rights": "labeled-for-nocommercial-reuse"},
    {"query": "images de video surveillance en ville", "image_directory": "surveillance",
     "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    # {"query": "Marseille places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse"},
    # {"query": "Marseille places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse-with-modifications"},
    # {"query": "Marseille places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-nocommercial-reuse"},
    # {"query": "Marseille places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    # {"query": "Paris places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse"},
    # {"query": "Paris places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse-with-modifications"},
    # {"query": "Paris places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-nocommercial-reuse"},
    # {"query": "Paris places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    # {"query": "Toulouse places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse"},
    # {"query": "Toulouse places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse-with-modifications"},
    # {"query": "Toulouse places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-nocommercial-reuse"},
    # {"query": "Toulouse places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    # {"query": "Nice places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse"},
    # {"query": "Nice places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse-with-modifications"},
    # {"query": "Nice places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-nocommercial-reuse"},
    # {"query": "Nice places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    # {"query": "Montpellier places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse"},
    # {"query": "Montpellier places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse-with-modifications"},
    # {"query": "Montpellier places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-nocommercial-reuse"},
    # {"query": "Montpellier places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    # {"query": "Nantes places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse"},
    # {"query": "Nantes places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse-with-modifications"},
    # {"query": "Nantes places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-nocommercial-reuse"},
    # {"query": "Nantes places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    # {"query": "Strasbourg places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse"},
    # {"query": "Strasbourg places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse-with-modifications"},
    # {"query": "Strasbourg places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-nocommercial-reuse"},
    # {"query": "Strasbourg places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    # {"query": "Bordeaux places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse"},
    # {"query": "Bordeaux places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse-with-modifications"},
    # {"query": "Bordeaux places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-nocommercial-reuse"},
    # {"query": "Bordeaux places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
    # {"query": "Lille places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse"},
    # {"query": "Lille places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-reuse-with-modifications"},
    # {"query": "Lille places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-nocommercial-reuse"},
    # {"query": "Lille places publiques vides", "image_directory": "background_en_cours2",
    #  "usage_rights": "labeled-for-noncommercial-reuse-with-modification"},
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
                 "limit": 250,
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
