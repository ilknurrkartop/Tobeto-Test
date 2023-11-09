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

Select e.employee_id,e.first_name,e.last_name
from employees e
inner join orders o ON e.employee_id = o.employee_id
where o.order_date BETWEEN DATE '1998-05-03' AND DATE '1998-05-04'