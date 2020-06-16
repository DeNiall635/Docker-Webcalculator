using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;

namespace webcalcmodullo.Controllers
{
    [ApiController]
    public class ErrorController : ControllerBase
    {
        [Route("/error")]
        public string error() { 
        var j1 = JsonConvert.SerializeObject(new
        {
            error = "true",
            String = "missing parameters",
            answer = "0"
        });


            return j1.ToLower();
        }

}
}