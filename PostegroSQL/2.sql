--join
--hangi ürün hangi kategoride
select products.product_name,categories.category_name from products
inner join categories ON products.category_id = categories.category_id

--hangi sipariş hangi kargo şirketi ile ne zaman gönderilmiştir?
--orders - shippers
select o. order_id,s.company_name,o.order_date from orders o
inner join shippers s on o.ship_via = s.shipper_id

--hangi siparişi hangi çalışan almış hangi müşteri vermiştir?
-- orders - employees - customers
select * from orders o
inner join employees e on o.employee_id = e.employee_id -- ordes'ın rightına customersın leftine
inner join customers c on o.customer_id = c.customer_id -- employee right


--left join
--çalışanın aldığı siparişler ve tarihleri listeleyelim
select employees.first_name,order_id,order_date from employees
left join orders on employees.employee_id = orders.employee_id

--right join
select employees.first_name,order_id,order_date from employees
right join orders on employees.employee_id = orders.employee_id

--full outer join
select c.contact_name from customers c
full outer join orders o on c.customer_id = o.customer_id

--group by

--her grubun toplam sipariş miktarını listeleyelim
select product_id,SUM(quantity) from order_details
group by product_id

--hangi kategoride kaç ürün var?
select category_name, count(*) from products p
inner join categories c on p.category_id = c.category_id
group by category_name

--hangi ülkeye ne kadarlık satış yapılmış ? 
select o.ship_country, SUM(od.quantity * od.unit_price) as total_price from orders o
inner join order_details od on o.order_id = od.order_id
group by o.ship_country
order by total_price desc

--having