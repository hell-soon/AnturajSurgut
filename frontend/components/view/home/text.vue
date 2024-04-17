<template>
  <div class="text">
    <img src="/public/img/home-view/cluboc.png" alt="cluboc">
    <h3>
      Мы специализируемся на продаже высококачественных тканей и аксессуаров,
      работая в тесном сотрудничестве с производителями
    </h3>
  </div>
</template>

<style scoped lang="scss">
.text {
  position: relative;
  width: 100%;
  height: 400px;
  display: flex;
  text-align: center;
  align-items: center;
  justify-content: center;
  overflow: visible;

  img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  h3 {
    max-width: 600px;
    color: black;
  }
}
</style>
