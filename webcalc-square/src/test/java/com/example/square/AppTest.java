	
package com.example.square;

import static org.junit.Assert.*;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.web.server.LocalServerPort;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.test.context.junit4.SpringRunner;

import static org.assertj.core.api.Assertions.assertThat;


@RunWith(SpringRunner.class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class AppTest {
	
	 @LocalServerPort
	    int randomServerPort;
	 
	    @Autowired
	    private TestRestTemplate restTemplate;
		
	    @Test
	    public void test_no_parameters()
	    {
	        String body = this.restTemplate.getForObject("/", String.class);
	        assertThat(body).isEqualTo("{\"string\":\"missing parameters\",\"answer\":0,\"error\":true}");
	   
	    }
	     
	    @Test
	    public void Two_parameters()
	    {
	        String body = this.restTemplate.getForObject("/?x=5&y=3", String.class);
	        assertThat(body).isEqualTo("{\"string\":\"5*5=25\",\"answer\":25,\"error\":false}");
	   
	    }
	    
	    @Test
	    public void One_parameter()
	    {
	        String body = this.restTemplate.getForObject("/?x=5", String.class);
	        assertThat(body).isEqualTo("{\"string\":\"5*5=25\",\"answer\":25,\"error\":false}");
	   
	    }
	    
	    @Test
	    public void One_negative_parameter()
	    {
	        String body = this.restTemplate.getForObject("/?x=-5", String.class);
	        assertThat(body).isEqualTo("{\"string\":\"-5*-5=25\",\"answer\":25,\"error\":false}");
	   
	    }
	    
	    @Test
	    public void Missing_x_parameter()
	    {
	        String body = this.restTemplate.getForObject("/?y=3", String.class);
	        assertThat(body).isEqualTo("{\"string\":\"missing parameters\",\"answer\":0,\"error\":true}");
	   
	    }
	    

	@Test
	public void test() {
		Squarefunction f = new Squarefunction();
		assertEquals(f.squarefunction(5), 25);
	}
	


}
