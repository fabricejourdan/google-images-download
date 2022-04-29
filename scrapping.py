# importing google_images_download module
from google_images_download import google_images_download

# creating object
response = google_images_download.googleimagesdownload()

search_items = [
    {"query": "parc a velo dans la ville de lyon", "usage_rights": "labeled-for-reuse"},
    {"query": "parc a velo dans la ville de lyon", "usage_rights": "labeled-for-reuse-with-modifications"},
]

# Driver Code
for search_item in search_items:
    query = search_item["query"]
    print('query:', query)
    usage_rights = search_item["usage_rights"]
    print('usage_rights:', usage_rights)
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
                 "limit": 300,
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
