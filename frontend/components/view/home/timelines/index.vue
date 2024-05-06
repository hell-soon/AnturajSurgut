<script setup lang="ts">
import { useDisplay } from 'vuetify'
import Timeline from '~/utils/mock/timelines'

const { sm, xs } = useDisplay()
</script>

<template>
  <section class="timelines">
    <h2 class="text-black">
      мы работаем по следующим направлениям
    </h2>
    <v-timeline :direction="sm || xs ? 'vertical' : 'horizontal'">
      <v-timeline-item
        v-for="(item, index) in Timeline"
        :key="index"
        dot-color="#138f87"
        icon="mdi-check"
        size="small"
      >
        <template #opposite>
          <span class="text-black body">{{ item.name }}</span>
        </template>
        <div>
          <v-lazy
            :options="{ threshold: 0.5 }"
            :transition="index === 0 || index === 2 ? 'slide-y-transition' : 'slide-y-reverse-transition'"
          >
            <p class="smallFootnote text-grey-darken-2">
              {{ item.text }}
            </p>
          </v-lazy>
        </div>
      </v-timeline-item>
    </v-timeline>
  </section>
</template>

<style scoped lang="scss">
.timelines {
  display: flex;
  flex-direction: column;
  gap: $cover-50;

  ul {
    display: flex;
    flex-direction: column;
    gap: 6px;

    li {
      list-style: '✔ ';
    }
  }
}
</style>
