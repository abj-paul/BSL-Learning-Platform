import { Component } from '@angular/core';
import { LoginService } from './login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  constructor(private loginService: LoginService){}

  loginStatus: boolean = false;

  authenticateAndPrint(){
    const userName = document.getElementsByTagName("input")[0].value ;
    const password = document.getElementsByTagName("input")[1].value ;

    console.log(userName, password);
    this.loginStatus = this.loginService.authenticate(userName, password);
    console.log("Login Status: "+this.loginStatus);
    //document.getElementsByTagName("span")[0].innerText = "Status:" + String(this.loginStatus);
  }
}
