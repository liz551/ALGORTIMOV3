package pe.edu.upc.controller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;


@Controller
@RequestMapping("/inicio")
public class InicioController {
	@RequestMapping("/bienvenido")
	public String irBienvenido() {
		
		return "bienvenido";
	}

	@RequestMapping("/login")
	public String irLogin() {
		
		return "login";
	}
	@RequestMapping("/logout")
	 public String irLogOut() {
			
			return "logout";
		} 
	@RequestMapping("/Miperfil")
	public String Miperil() {
		
		return "Miperfil";
	}
	
}
