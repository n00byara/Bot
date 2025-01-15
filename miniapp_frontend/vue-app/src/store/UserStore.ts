import { defineStore } from "pinia"

export const usersStore = defineStore("users", {
    state: () => ({ users: Array() }),
})