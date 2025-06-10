document.addEventListener('DOMContentLoaded', function () {
  const selectTipo = document.getElementById('tipo_usuario');
  const campoRA = document.getElementById('ra-campo');
  const campoUC = document.getElementById('uc-campo');
  const campoInstituicaoMatriz = document.getElementById('instituicao_matriz-campo');
  const campoNomeProjeto = document.getElementById('nome_projeto-campo');
  const campoTemaTrabalho = document.getElementById('tema_trabalho-campo');

  function atualizaCamposEmTela() {
    switch (selectTipo.value) {
      case '1':
        campoRA.style.display = 'block';
        campoUC.style.display = 'block';
        campoInstituicaoMatriz.style.display = 'none';
        campoNomeProjeto.style.display = 'none';
        campoTemaTrabalho.style.display = 'none';
        break;
      case '2':
        campoRA.style.display = 'block';
        campoUC.style.display = 'block';
        campoInstituicaoMatriz.style.display = 'none';
        campoNomeProjeto.style.display = 'block';
        campoTemaTrabalho.style.display = 'block';
        break;
      case '3':
        campoRA.style.display = 'block';
        campoUC.style.display = 'block';
        campoInstituicaoMatriz.style.display = 'none';
        campoNomeProjeto.style.display = 'none';
        campoTemaTrabalho.style.display = 'none';
        break;
      case '4':
        campoRA.style.display = 'block';
        campoUC.style.display = 'block';
        campoInstituicaoMatriz.style.display = 'none';
        campoNomeProjeto.style.display = 'block';
        campoTemaTrabalho.style.display = 'block';
        break;
      case '5':
        campoRA.style.display = 'block';
        campoUC.style.display = 'none';
        campoInstituicaoMatriz.style.display = 'block';
        campoNomeProjeto.style.display = 'block';
        campoTemaTrabalho.style.display = 'block';
        break;
      case '6':
        campoRA.style.display = 'none';
        campoUC.style.display = 'none';
        campoInstituicaoMatriz.style.display = 'none';
        campoNomeProjeto.style.display = 'none';
        campoTemaTrabalho.style.display = 'none';
        break;
    }
  }

  atualizaCamposEmTela();

  selectTipo.addEventListener('change', atualizaCamposEmTela);
});