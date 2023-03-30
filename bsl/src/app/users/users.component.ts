import { Component, OnInit } from '@angular/core';
import { LoginCredential } from '../login/login.credential';
import { LoginService } from '../login/login.service';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})
export class UsersComponent implements OnInit {
  constructor(private loginService: LoginService){}
  userList: LoginCredential[] = [];

  ngOnInit(): void {
    this.userList = this.loginService.getUserList();
  }

  
  
}
