<script setup lang="ts">
import SelectCatalog from './select-catalog.vue'
import SelectSubcatalog from './select-subcatalog.vue'
import SelectColor from './select-color.vue'
import SelectSize from './select-size.vue'
import SelectCompound from './select-compound.vue'
import PriceInpuit from './price-input.vue'
import { watchParam } from '~/utils/helpers/filters'

const store = setupStore(['productList'])

watchParam('high_rating', 'high_rating', undefined)
watchParam('most_sold', 'most_sold', undefined)
</script>

<template>
  <v-card
    title="Фильтры"
    class="card"
    elevation="3"
  >
    <div>
      <v-checkbox
        v-model="store.productList.params.high_rating"
        label="По популярности"
        hide-details
      />
      <v-checkbox
        v-model="store.productList.params.most_sold"
        label="Самые продаваемые"
      />
      <v-expansion-panels
        variant="accordion"
        multiple
      >
        <v-expansion-panel
          title="Цена"
        >
          <v-expansion-panel-text>
            <PriceInpuit />
          </v-expansion-panel-text>
        </v-expansion-panel>

        <v-expansion-panel
          title="Каталог"
        >
          <v-expansion-panel-text>
            <SelectCatalog />
            <SelectSubcatalog />
          </v-expansion-panel-text>
        </v-expansion-panel>

        <v-expansion-panel
          title="Парамаетры"
        >
          <v-expansion-panel-text>
            <SelectColor />
            <SelectSize />
            <SelectCompound />
          </v-expansion-panel-text>
        </v-expansion-panel>
      </v-expansion-panels>
    </div>
  </v-card>
</template>

<style scoped lang="scss">
.card {
  position: sticky !important;
  top: 10px;
}
</style>
