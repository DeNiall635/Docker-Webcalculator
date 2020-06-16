package com.example.square;

import org.springframework.boot.web.servlet.error.ErrorController;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import net.minidev.json.JSONObject;

@Controller
public class MyErrorController implements ErrorController {
	
	    @RequestMapping("/error")
	    @ResponseBody
	    public String handleError() {
	    	 JSONObject objerror = new JSONObject();
	         objerror.put("error", true);
	         objerror.put("string", String.format("missing parameters"));
	         objerror.put("answer", 0);

	         return objerror.toString();
	    }
	    
	    @Override
	    public String getErrorPath() {
	    	return "/error";
	    }
	    
	}
