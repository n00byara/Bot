import type { AxiosResponse } from "axios"

import { HttpService } from "@/services/HttpService"
import { usersStore } from "@/store/UserStore"
import type { IUserInfo } from "@/interfaces/IUserInfo"

export class UsersApiService {
    private http: HttpService = new HttpService()

    private state = usersStore()

    public async getUsers() {
        this.http.get<AxiosResponse>("").then((response: AxiosResponse) => {
            const data: Array<IUserInfo> = response.data
            
            this.state.users = data
        })
    }
} 