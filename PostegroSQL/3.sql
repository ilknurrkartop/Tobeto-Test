--EXISTS / NOT EXISTS (mevcut mu?)

--ürün fiyatı 20 den küçük olan tedarikçileri listeler
Select company_name from suppliers
where EXISTS(Select product_name from products
			where suppliers.supplier_id=products.supplier_id
			AND unit_price<20)
			
Select company_name from suppliers
where NOT EXISTS(Select product_name from products
			where suppliers.supplier_id=products.supplier_id
			AND unit_price=20)

--'3/5/1998' ile '4/5/1998' tarihleri arasında sipariş almış çalışanları listeliyoruz.

