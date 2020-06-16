package com.example.square;
import com.example.square.Squarefunction;

import net.minidev.json.JSONObject;
import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.web.bind.annotation.*;

@SpringBootApplication
@RestController
public class App {

	@GetMapping("/")
    String square(@RequestParam("x") int x){
		
		Squarefunction s = new Squarefunction();
		int answer = s.squarefunction(x);
      
      JSONObject obj = new JSONObject();
      obj.put("error", false);
      obj.put("string", String.format("%d*%d=%d", x,x, answer));
      obj.put("answer", answer);

      return obj.toString();
    }


	public static void main(String[] args) {
		SpringApplication.run(App.class, args);
	}
}