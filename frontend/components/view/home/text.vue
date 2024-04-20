<template>
  <div class="block">
    <img class="img top" src="/public/img/home-view/zavetuscha-top.png" alt="zavetuscha">
    <div class="text">
      <img src="/public/img/home-view/cluboc.png" alt="cluboc">
      <h3 class="text-black">
        Мы специализируемся на продаже высококачественных тканей и аксессуаров,
        работая в тесном сотрудничестве с производителями
      </h3>
    </div>
    <img class="img bottom" src="/public/img/home-view/zavetuscha-bottom.png" alt="zavetuscha">
  </div>
</template>

<style scoped lang="scss">
.text {
  position: relative;
  width: 100%;
  height: 310px;
  display: flex;
  text-align: center;
  align-items: center;
  justify-content: center;

  img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  h3 {
    max-width: 540px;
  }
}

.block {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 100%;

  .img {
    top: 0;
    width: 1440px;
  }

  .top {
    padding-bottom: 20px;
  }
}
</style>
