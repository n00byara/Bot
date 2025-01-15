import axios from "axios"

import { Config } from "@/configuration/Config"

const config = new Config()

export class HttpService {
    public async get<TRes>(uri: string): Promise<TRes> {
        return await axios.get(`${config.url}/${uri}`)
    }

    public async post<TRes, TPay>(uri: string, data: TPay): Promise<TRes> {
        return await axios.post(`${config.url}${uri}`, data)
    }
}