<template>
  <div class="credits">
    <NavSearchBox q="a"/>

    <div class="w-100 mt-5">
      <div class="row justify-content-center">
          <h1>Desarrolladores</h1>
          <table class="table d-flex justify-content-center ">
            <tr class="d-block justify-content-center">
              <td class="w-50 "> 
                <div class="card shadow border-less p-0">
                  <!-- Ariel Info -->
                  <div class="card-body">
                    <a class="credit-name" href="https://github.com/ArielTriana">
                      <img height='100' src="https://images.weserv.nl/?url=avatars.githubusercontent.com/u/61637781?v=4&h=300&w=300&fit=cover&mask=circle"/>
                      <br/>
                      Ariel Alfonso Triana Pérez
                    </a>
                    <br/>
                    <small><strong>Classroom:</strong> C311</small>
                  </div>
                  <div class="card-footer border-less">
                    <a href="https://github.com/ArielTriana" target="_blank"><i class="fab fa-github"></i></a> 
                    &nbsp;&nbsp;&nbsp;&nbsp;
                    <a href="http://t.me/atp_ariel" target="_blank"><i class="fab fa-telegram"></i></a> 
                    &nbsp;&nbsp;&nbsp;&nbsp;
                    <a href="mailto:ariel.triana@estudiantes.matcom.uh.cu"><i class="fas fa-envelope"></i></a>
                  
                  </div>
                </div>
              </td>

              <td class="w-50">
                <div class="card shadow border-less p-0">
                  <!-- Frank Info -->
                  <div class="card-body">
                    <a class="credit-name" href="https://github.com/FrankBlanco1">
                      <img src="https://images.weserv.nl/?url=avatars.githubusercontent.com/u/62571934?v=4&h=300&w=300&fit=cover&mask=circle" height="100" />
                      <br/>
                      Frank Abel Blanco Gómez  
                    </a>
                    <br/>
                    <small><strong>Classroom:</strong> C312</small>
                  </div>
                  <div class="card-footer border-less">
                    <a href="https://github.com/FrankBlanco1" target="_blank"><i class="fab fa-github"></i></a> 
                    &nbsp;&nbsp;&nbsp;&nbsp;
                    <a href="http://t.me/frank1423" target="_blank"><i class="fab fa-telegram"></i></a> 
                    &nbsp;&nbsp;&nbsp;&nbsp;
                    <a href="mailto:frank.abel@estudiantes.matcom.uh.cu"><i class="fas fa-envelope"></i></a>
                  </div>
                </div>
              </td>
            </tr>
          </table>
      </div>
    </div>
  </div>
</template>

<script>
import NavSearchBox from "@/components/NavSearchBox.vue"

export default {
  name: 'Credits',
  components: {
    NavSearchBox
  }
}
</script>
<style scoped>
.border-less {
  border-width: 0px !important;
}

.credit-name
{
  color: black;
}

.credit-name:hover,
.credit-name:focus,
.credit-name:active
{
  color: gray;
  text-decoration: none;
}
</style>