#iZettle CSV Product Importer

This simple Python script was written to allow you to simply import a CSV into iZettle so that you don't have to manually create the products. The script using selenium which is a web browser automation framework. If iZettle change the structure of thier website this could break the script and it will require updating. The script was created using Python 3.4.* with the selenium framework but may be backwards compatible.

Currently this importer does not support additional variants or image uploads, the script was only written to meet my needs but is open source and free for anyone to build on. If you develop please push back!

##Setup
To configure it you need to enter your credentials in `self.username` and `self.password`, the username must be the main account holder as staff accounts do not have permission to create products. Next you need to configure `self.csvfilename` to be the name of your csv in the same directory as the script. All these configurations are next to each other near the top of the script, something like below.

```python
        #Configure these
        self.username = "email@domain.com"          #Your iZettle Admin Email Address (Admin require to add products)
        self.password = "Password123"               #Your iZettle Password
        self.csvfilename = "dummy.csv"              #Your csv file containing products
```

##CSV
You will find a dummy CSV file in the repository, please note that the CSV has no headers. The file must be in the order of fields as follows...

`Name, Variant, Price, Barcode, Price, Tax`

Name is the name of the product.
Variant is Size/Colour etc of the product.
Price is the price without currency example `9.99`, the currency is set in your iZettle settings.
Barcode is the barcode, product id or sku of the product.
Tax is the tax percentage of the product for example 20% would be `20`.

##Running
Once you have configured the script and your CSV navigate to the directory and execute
`py Import.py`
No additional parameters are required.


