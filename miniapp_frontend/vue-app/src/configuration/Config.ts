import { URL } from "#/Constants"

export class Config {
    static instance = new Config()

    constructor() {
        if (Config.instance) {
            return Config.instance;
        }

        Config.instance = this;
      
        Object.freeze(this);
    }

    get url(): string {
        return URL
    }
}