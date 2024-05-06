<script setup lang="ts">
import { useDisplay } from 'vuetify'
import type { Review } from '~/types/models/review'

const props = defineProps<{ info: Review }>()
const { sm, xs } = useDisplay()
const rating = props.info.rating
</script>

<template>
  <div class="card">
    <div class="card-haeder">
      <div class="card-haeder__name">
        <span class="body text-black">
          {{ info.user.first_name }} {{ info.user.last_name }}
        </span>
      </div>
      <span class="smallFootnote text-grey-darken-2">{{ info.created_at }}</span>
    </div>
    <div class="card-content">
      <p class="footnote text-black">
        {{ info.text }}
      </p>
    </div>
    <div class="card-footer">
      <v-rating
        v-model="rating"
        color="orange-lighten-2"
        active-color="orange-lighten-1"
        readonly
        :density="sm || xs ? 'comfortable' : 'default'"
      />
    </div>
  </div>
</template>

<style scoped lang="scss">
.card {
  display: flex;
  flex-direction: column;
  gap: $cover-16;
  padding: clamp($cover-16, 5vw, $cover-24);
  border-radius: $cover-12;
  box-shadow: $shadow-card-review;
  margin: $cover-30 $cover-24;
  height: 400px;

  &-content {
    display: flex;
    align-items: flex-start;
    overflow: hidden;

    p {
      -webkit-line-clamp: 9;
      -webkit-box-orient: vertical;
      display: -webkit-box;
    }
  }

  &-footer {
    margin-top: auto;
  }
}
</style>
