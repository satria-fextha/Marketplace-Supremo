El Filepath es: /c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/devoluciones_y_reembolsos/políticas.py
class PoliticasDevolucionesReembolsos:
    def __init__(self):
        self.politicas = {
            'producto_defectuoso': {
                'descripcion': 'Si el producto está defectuoso, se puede solicitar una devolución o reembolso.',
                'requisitos': 'El producto debe estar en su estado original y se debe solicitar dentro de los 30 días de la compra.',
                'proceso': 'El consumidor debe completar un formulario de solicitud de devolución/reembolso. El vendedor es notificado y se coordina la devolución o se procesa el reembolso.'
            },
            'producto_incorrecto': {
                'descripcion': 'Si se recibió un producto incorrecto, se puede solicitar una devolución o reembolso.',
                'requisitos': 'El producto debe estar sin usar y en su empaque original. Se debe solicitar dentro de los 15 días de la compra.',
                'proceso': 'El consumidor debe comunicarse con el vendedor y proporcionar detalles sobre el producto incorrecto. El vendedor es notificado y se coordina la devolución o se procesa el reembolso.'
            },
            'cambio_de_opinion': {
                'descripcion': 'Si el consumidor cambia de opinión sobre la compra, se puede solicitar un reembolso.',
                'requisitos': 'El producto debe estar sin usar y en su empaque original. Se debe solicitar dentro de los 7 días de la compra.',
                'proceso': 'El consumidor debe completar un formulario de solicitud de reembolso. El vendedor es notificado y se procesa el reembolso.'
            }
        }

    def consultar_politica(self, tipo_producto):
        if tipo_producto in self.politicas:
            return self.politicas[tipo_producto]
        else:
            return 'No se encontró una política para el tipo de producto especificado.'


politicas = PoliticasDevolucionesReembolsos()
