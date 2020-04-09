import requests
import bs4
import csv

response = requests.get('http://yayvo.com/')
soup = bs4.BeautifulSoup(response.text, 'html.parser')
# print(soup)

mainRoot = soup.find(class_="ma-tabsproduct-contain").find(class_="ma-tabs-content")
posts = mainRoot.findAll(class_="flexslider carousel")
# print(posts)

Product_List = []
# Working on HTML Text
print(['Product Category', 'Link', 'Name', 'New Price', 'Old Price', 'Discount', 'Image Source'])
for post in posts:
    product_Class = post.findAll(class_="newproductslider-item")
    # print(product_Class)
    for products in product_Class:
        # Product Link
        Product_Link = products.find(class_="product-image rel-pos")['href']
        # Product Discount
        try:
            Product_Discount = products.find(class_="discount_Span").get_text().replace("-", "")
        except AttributeError:
            Product_Discount = "None"
        # Product Image
        Product_Image = products.find(class_="b-lazy")['data-src']
        # print(Product_Link, Product_Discount, Product_Image)
        # Product New Price
        try:
            NewPrice = products.find(class_="custom_pricespec").find(class_="price").get_text().replace("  ", "")
        except AttributeError:
            NewPrice = products.find(class_="custom_pricereg").find(class_="price").get_text().replace("  ", "")
        # Product Old Price
        try:
            OldPrice = products.find(class_="custom_pricedisc").find(class_="price").get_text().replace("  ", "")
        except AttributeError:
            OldPrice = "None"
        # print(NewPrice, OldPrice)
        # Product Category
        Product_Category = products.find(class_="cstm_brnd").find("span").get_text()
        # Product Name
        Product_Name = products.find(class_="custom_prodname")["title"]
        # print(Product_Category, Product_Name)

        Product_List.append([str(Product_Category), str(Product_Link), str(Product_Name), str(NewPrice), str(OldPrice), str(Product_Discount), str(Product_Image)])
        # print([str(Product_Category), str(Product_Link), str(Product_Name), str(NewPrice), str(OldPrice), str(Product_Discount), str(Product_Image)])
        # csv_writer.writerow(Product_List)

print("Total Products:", len(Product_List))


# CSV File
with open('Scrapped_Data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    headers = ['Product Category', 'Product Link', 'Name', 'New Price', 'Old Price', 'Discount', 'Image Source']
    writer.writerow(headers)
    for products in range(len(Product_List)):
        print(Product_List[products])
        writer.writerow(Product_List[products])

# End of Program
