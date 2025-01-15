<script setup lang="ts">
import { onMounted } from "vue"
import { UsersApiService } from "@/services/UsersApiService"
import { usersStore } from "@/store/UserStore"

const store = usersStore()

const usersApiService = new UsersApiService()

onMounted(() => {
    usersApiService.getUsers()
})
</script>

<template>
    <div class="item">
      <p>{{ store.users }}</p>
    </div>
</template>

<style scoped>
</style>