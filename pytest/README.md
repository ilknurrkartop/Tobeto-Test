
Pytest, Python dilindeki testlerin yazılması ve yürütülmesi için kullanılan bir test çerçevesidir. Pytest, test fonksiyonlarına ve test davranışlarına özel işlevselliği eklemek ve kontrol etmek için çeşitli decorator'ları sağlar. 
İşte Pytest'te kullanılan bazı yaygın decorator'ler:
@pytest.fixture:

Fixture'lar, testler arasında veri paylaşımını sağlar ve test süreçlerini düzenler.
Bir fixture, bir fonksiyonun başlangıç durumunu ayarlamak ve testin sonunda temizlik yapmak için kullanılabilir.
Parametre olarak alınan fonksiyon içerisinde hazırlıklar yapılır ve bu fonksiyonun sonucu, test fonksiyonlarına geçilir.
python
Copy code
import pytest

@pytest.fixture
def example_data():
    return {'key': 'value'}

def test_using_fixture(example_data):
    assert example_data['key'] == 'value'
@pytest.mark.parametrize:

Parametrize decorator'ü, bir test fonksiyonunu farklı parametre setleri ile birden çok kez çalıştırmak için kullanılır.
Her bir parametre seti, testin farklı durumlarını temsil eder.
python
Copy code
import pytest

@pytest.mark.parametrize("input, expected", [(1, 2), (2, 4), (3, 6)])
def test_multiply_by_two(input, expected):
    result = input * 2
    assert result == expected
@pytest.mark.skip ve @pytest.mark.skipif:

@pytest.mark.skip: Bir testin belirli bir koşul altında atlanmasını sağlar.
@pytest.mark.skipif: Belirli bir koşul sağlandığında bir testin atlanmasını sağlar.
python
Copy code
import pytest
import sys

@pytest.mark.skip(reason="Geçici olarak atlandı")
def test_example_skip():
    assert 1 + 1 == 2

@pytest.mark.skipif(sys.version_info < (3, 6), reason="Sadece Python 3.6 ve üstü destekleniyor")
def test_example_skipif():
    assert 1 + 1 == 2
@pytest.mark.xfail:

Bir testin başarısız olması bekleniyorsa kullanılır. Ancak, bu durum testin sonucunu etkilemez ve test hala geçerli sayılır.
Kullanıcı, bir testin başarısız olması bekleniyorsa ancak başarılı olursa uyarı alır.
python
Copy code
import pytest

@pytest.mark.xfail
def test_example_xfail():
    assert 1 + 1 == 3
Bu decorator'lar, Pytest'in temel özelliklerinden sadece birkaçıdır. Pytest, daha fazla özelliğe ve decorator'a sahiptir ve bu özellikleri ihtiyacınıza göre kombinleyebilirsiniz. 
