import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.kiryano.com/home.php?pid=65')
soup = BeautifulSoup(response.text, 'html.parser')

mainRoot = soup.find(class_="shop-page-container mb-50").find(class_="container").find(class_="row").find(class_="col-lg-9 order-1 order-lg-2 mb-sm-35 mb-xs-35")
posts = mainRoot.find(class_='shop-product-wrap grid row no-gutters mb-35').findAll(class_='col-xl-3 col-lg-4 col-md-4 col-sm-6 col-6')

with open('ProductScrapped.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Product Category', 'Product Link', 'Name', 'New Price', 'Old Price', 'Discount', 'Image Source']
    csv_writer.writerow(headers)

    for post in posts:
        findProductLink = post.find(class_="gf-product shop-grid-view-product").find(class_="image").find('a')['href']
        findProductDiscount = post.find(class_="gf-product shop-grid-view-product").find(class_="image").find(class_="onsale").get_text().replace(' Off', '')
        findImageSource = post.find(class_="gf-product shop-grid-view-product").find(class_="image").find('img')['src']
        print(findProductLink)

        findProductContent = post.find(class_="gf-product shop-grid-view-product").find(class_="product-content")
        findProductTitle = findProductContent.find(class_="product-title").find('a').get_text()
        findProductNewPrice = findProductContent.find(class_="price-box").find(class_="discounted-price").get_text()
        findProductOldPrice = findProductContent.find(class_="price-box").find(class_="main-price").get_text()

        findProductCategory = findProductContent.find(class_="product-categories")
        # If Category count increase then manual work require
        categoryList = findProductCategory.findAll('a')
        category1 = categoryList[0].get_text()
        category2 = categoryList[1].get_text()
        ProductCategory = category1 + ", " + category2

        print(ProductCategory, findProductLink, findProductTitle, findProductNewPrice, findProductOldPrice, findProductDiscount, findImageSource)
        csv_writer.writerow([ProductCategory, findProductLink, findProductTitle, findProductNewPrice, findProductOldPrice, findProductDiscount, findImageSource])

# End of Program