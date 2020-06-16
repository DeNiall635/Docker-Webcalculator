using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;

namespace webcalcmodulo.Controllers
{
    [Route("/")]
    [ApiController]
    public class ValuesController : ControllerBase
    {
        // GET api/values
        [HttpGet]
        public string Get([FromQuery(Name = "x")] int x, [FromQuery(Name = "y")] int y)
        {
            Modulofunction m = new Modulofunction();
            int answer = m.Modulo(x, y);

            var j = JsonConvert.SerializeObject(new
            {
                error = "false",
                String = "",
                answer = answer
            });


            return j.ToLower();
        }

    }


}
