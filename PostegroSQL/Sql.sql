--SQL = Structured Query Language
--Veri Sorgulama - Veri Manipülasyonu

--SELECT
--Select [kolonlar]/* from[tablo_adi]

Select * from products;
Select product_name, unit_price from products;

--WHERE
--'den 'dan anlamları katar
--filtreleme

Select * from products where unit_price >50;
Select * from products where unit_price >50 AND unit_price <100;
Select * from products where unit_price BETWEEN 50 AND 100;
Select product_name,category_id,unit_price from products where unit_price >=50 OR category_id >5;
Select * from products where product_name= 'Chai' OR product_name='Chang' OR product_name= 'Ikura';

--IN()
--İçerisine parametre olarak verilen n kadar veri ile ilgili alanın uyuşmasını bekler.

Select * from products where product_name IN('Chai','Chang','Ikura');
Select * from products where category_id In(1,2,3);

--LIKE
--kalıba benzeyen ifadeleri getirir.
-- % => ilgili metnin sol ya da sağında eklendiğinde
--sağ ve sol için metinden sonra gelecek metni önemsiyorum.
--İsminin içerisinde 't' harfi geçen tüm ürünleri
Select * from products where LOWER(product_name) LIKE 't%'

-- _  =>karakter olarak geçer.
Select * from products where product_name LIKE '__r%';--son harfi r olan ürünleri getirmiş oldui

--BUILD-IN FUNCTIONS
--SUMMARY => TOPLAMA
Select SUM(unit_price) from products

--AVERAGE => ORTALAMA
Select AVG(unit_price) from products

--MAXIMUM => Verilerim arasından maksimum değeri döner
Select MAX(unit_price) from products

--MINIMUM => Verilerim arasından minumum değeri döner
Select MIN(unit_price) from products

--COUNT => Adet döndürür
Select COUNT(*) from products where unit_price >50; --vount olasaydı 50 üstü ürünü 7 tane listelerdi ama cpunt olduğu için sadece 7 sayısını gösterir


--DISTINCT => Tekraralrı engeller
--kaç farklı şehirden çalışanım var?
Select DISTINCT city  from employees

--SUB-QUERY ALT aorgular, iç içe sorgu
--Ortalamanın altında bir fiyata sahip olan ürünlerimin bilgisini istiyorum.

Select AVG(unit_price) from products --normal
Select * from products where unit_price < 28.83--normal
--şimdi altsorgusunu yazıyoruz

select * from products
where unit_price < (Select AVG(unit_price) from products)--parantez içerisi 28.83 küsürat sayı oluyor. sonra komuta göre listeliyor. iç içe sorgu budur

--En pahalı ürünümün bilgilerini getirelim
select MAX(unit_price) from products --en pahalı ürün 
select * from products where unit_price = 263.5 --ürünün bilgileri

select * from products
where unit_price = (select MAX(unit_price) from products)

--ORDER BY => sıralama
--default olarak => küçükten büyüğe sıralama
--ASCENDING => ASC => küçükten büyüğe a-z
--DESCENDING => DESC => büyükten küçüğe z-a
select product_name, unit_price from products
order by unit_price ASC

select product_name, unit_price from products
order by unit_price DESC

---now date
select current_date as "Bugünün Tarihi"
select date_part('month',current_date)
select date_part('year',current_date)


--GETDATE() => GÜNCEL TARİHİ-SAATİ
--DATEDIFF('interval'(year),date1,date2) => iki tarih arasındaki interval'e göre farkı verir

