package com.example.square;

import net.minidev.json.JSONobject;
import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.web.bind.annotation.*;

@SpringBootApplication
@restController
public class App {

    @GetMapping("/")
    String square(@RequestParam("x") int x){
      if(!checkIfNumberIsValid(x)){
        return "Number format is incorrect, please use whole numbers only."
      }

      int answer = x * x
      JSONobject obj = new JSONobject();
      obj.put("error", false);
      obj.put("String", String.format("%d*%d", x, answer));
      obj.put("answer", answer);

      return obj.toString();
    }


    public static void main(String[] args) { SpringApplication.run(App.class, args);}
}
