using NUnit.Framework;
using webcalcmodulo;
using webcalcmodulo.Controllers;

namespace webcalc_moduloTest
{
    public class Tests
    {

        [Test]
        public void ModuloTest()
        {
            Modulofunction f = new Modulofunction();
            int answer = f.Modulo(7, 2);
            int expected = 1;
            Assert.AreEqual(answer, expected);
        }

    }
}