import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EditUserInfoComponent } from './edit-user-info/edit-user-info.component';
import { LoginComponent } from './login/login.component';
import { ProfileComponent } from './profile/profile.component';
import { UsersComponent } from './users/users.component';

const routes: Routes = [
  {path:"users", component:UsersComponent},
  {path:"profile", component:ProfileComponent},
  {path: "login", component: LoginComponent},
  {path: "editInfo", component: EditUserInfoComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
