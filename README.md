# TRABALHO 1: MOVIMENTO DE CORPO RÍGIDO E PROJEÇÃO PINHOLE COM INTERFACE GRÁFICA

## ORIENTAÇÕES PARA O DESENVOLVIMENTO:

* Visualizar a posição e orientação tridimensional de uma câmera e de um objeto.

* Alterar a posição e orientação da câmera (parâmetros extrínsecos) através de translações e rotações tridimensionais. ATENÇÃO: O objeto não precisa ser movimentado, apenas a câmera.

* As translações e rotações poderão ser feitas tanto em relação ao referencial do mundo quanto em relação ao referencial próprio da câmera.

* Visualizar a imagem do objeto gerada pela câmera.

* Alterar os parâmetros intrínsecos da câmera (distância focal e fator de escala de cada eixo). Não precisa alterar o ponto principal, mas se certifique que a origem dos eixos da imagem se encontram no canto superior esquerdo!!! 

* Toda vez que algo for alterado, a visualização 3D e a imagem gerada pela câmera deverão ser atualizadas.

## VERSÕES DAS BIBLIOTECAS

* PySide6 => 6.5.0

* matplotlib => 3.7.1

## FUNCIONAMENTO GERAL

### LOGIN

* Na tela de Login, deve ser digitado "visao" no campo usuário e "2023-01" no campo senha para ter acesso ao sistema.

### MENUS NA TELA PRINCIPAL

* O menu permite alterar e visualizar as informações da câmera;

* No meu esquerdo é possível configurar a câmera:

	* DISTÂNCIA FOCAL em mm, TAMANHO CCD em mm e TAMANHO DA IMAGEM em pixels;

* Para realizar tal alteração é necessário escrever o valor numérico dentro das caixas correspondentes e clicar em ALTERAR para aplicar as mudanças;

* O não preenchimento de qualquer parâmetro mantém o mesmo com o valor atual;

* Valor default é:
	1. Distância Focal 	= 10mm
	2. Tamanho CCD 		= 36 x 24 mm
	3.Tamanho da imagem 	= 1280 x 720 pixels

* Após qualquer alteração é possível retornar ao valor default clicando no botão RESET.

* No menu à direita é possível movimentar a câmera;

* Para realizar tal alteração é necessário escrever o valor numérico dentro das caixas correspondentes e clicar em TRANSFORMAR para aplicar a rotação e a translação pretendidas na câmera;

* Ambas as transformações podem ser executadas tendo como referencial tanto o sistema de coordenadas da câmera quanto o do mundo, bastando alterar a caixa de seleção para alterar entre os sistemas de coordenadas;

* Caso mais de uma transformação seja solicitada na mesma ação a ordem de precedência a seguir será respeitada:
	1. Rotação em relação ao eixo X do referencial selecionado;
	2. Rotação em relação ao eixo Y do referencial selecionado;
	3. Rotação em relação ao eixo Z do referencial selecionado;
	4. Translação ao longo do referencial selecionado.

* O não preenchimento de qualquer parâmetro mantém o mesmo com o valor atual;

* Note que a rotação é dada em GRAUS, enquanto a TRANSLAÇÃO é dada em unidades do sistema de plotagem.

* A posição inicial da câmera é:
	1. [POSx, POSy, POSz] = [15,-5,6] nas coordenadas do mundo;
	2. ROTx = -90º rotacionados em relação ao eixo X do referencial do mundo;
	3. Sem rotação em em relação ao eixo Y do referencial do mundo;
	4. ROTz = 90º rotacionados em relação ao eixo Z referencial do mundo.

* Após qualquer transformação é possível retornar a câmera à sua posição inicial clicando no botão RESET.

### EXIBIÇÃO NA TELA PRINCIPAL

* A tela de exibição a esquerda exibe uma visualização 3D da cena, contendo o objeto e a câmera;

* A tela de exibição a direita exibe a visualização 2D da imagem gerada pela câmera, de acordo com sua configuração e posicionamento.
